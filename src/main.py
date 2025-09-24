#!/usr/bin/env python3
"""Execução paralela MPI para cálculo de métricas de grafos.
Suporta: centrality (degree_centrality), communities (girvan_newman small sample), sim_fail (simulação de remoção de nós).
Uso:
mpirun -np 4 python3 src/main.py --input data_sample/graph_sample.edgelist --metric centrality
"""
from mpi4py import MPI
import argparse, time, sys, json
import networkx as nx
from utils import load_graph, save_results, timed

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def compute_degree_centrality_partition(G, nodes):
    # networkx.degree_centrality computes on full graph; we compute only for requested nodes
    full = nx.degree_centrality(G)
    return {n: full.get(n, 0.0) for n in nodes}

def simulate_failure(G, nodes_to_remove):
    G2 = G.copy()
    G2.remove_nodes_from(nodes_to_remove)
    # return number of connected components after removal
    return nx.number_connected_components(G2)

def detect_communities_small(G, num_comms=5):
    # Using Girvan-Newman generator but stopping early (small graphs)
    comp = nx.community.girvan_newman(G)
    limited = []
    try:
        for i, c in enumerate(comp):
            limited = list(c)
            if i+1 >= num_comms:
                break
    except Exception:
        pass
    return limited

def chunk_list(lst, k):
    return [lst[i::k] for i in range(k)]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--metric", choices=['centrality','communities','sim_fail'], default='centrality')
    parser.add_argument("--remove_top", type=int, default=5, help="para sim_fail, quantos nós remover")
    args = parser.parse_args()

    if rank == 0:
        G = load_graph(args.input)
        nodes = list(G.nodes())
        chunks = chunk_list(nodes, size)
    else:
        G = None
        chunks = None

    # Broadcast graph and scatter chunks
    G = comm.bcast(G, root=0)
    chunks = comm.bcast(chunks, root=0)
    my_nodes = comm.scatter(chunks, root=0)

    t0 = time.time()
    local_result = {}
    if args.metric == 'centrality':
        local_result = compute_degree_centrality_partition(G, my_nodes)
    elif args.metric == 'communities':
        # only run communities on rank 0 to avoid heavy duplication (example)
        if rank == 0:
            local_result = {"communities": detect_communities_small(G, num_comms=5)}
        else:
            local_result = {}
    elif args.metric == 'sim_fail':
        # rank 0 computes centrality to choose top nodes, broadcasts list
        if rank == 0:
            central = nx.degree_centrality(G)
            top = sorted(central.items(), key=lambda x: x[1], reverse=True)[:args.remove_top]
            top_nodes = [n for n,_ in top]
        else:
            top_nodes = None
        top_nodes = comm.bcast(top_nodes, root=0)
        # every rank simulates removal of the same nodes on its local copy for measurement
        local_result = {"components_after_removal": simulate_failure(G, top_nodes)}
    t1 = time.time()

    gathered = comm.gather(local_result, root=0)

    if rank == 0:
        # merge results
        merged = {}
        for g in gathered:
            if isinstance(g, dict):
                merged.update(g)
        merged['meta'] = {'procs': size, 'time_s': t1-t0}
        # save
        out_path = "results/metrics_result.json"
        save_results(out_path, merged)
        print(f"Salvo resultados em {out_path}")
        print(json.dumps(merged, indent=2))

if __name__ == '__main__':
    main()
