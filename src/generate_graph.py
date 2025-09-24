#!/usr/bin/env python3
"""Gera um grafo sintético e salva em formato edgelist.
Exemplo:
python src/generate_graph.py --nodes 1000 --prob 0.01 --out data_sample/graph_sample.edgelist
"""
import argparse
import networkx as nx

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--nodes", type=int, default=1000)
    p.add_argument("--prob", type=float, default=0.01)
    p.add_argument("--out", type=str, default="data_sample/graph_sample.edgelist")
    args = p.parse_args()
    G = nx.erdos_renyi_graph(args.nodes, args.prob, seed=42)
    nx.write_edgelist(G, args.out, data=False)
    print(f"Gerado {args.out} com {args.nodes} nós e p={args.prob}")

if __name__ == '__main__':
    main()
