import networkx as nx
import time, json
def load_graph(path):
    G = nx.read_edgelist(path)
    return G

def save_results(path, obj):
    with open(path, 'w') as f:
        json.dump(obj, f, indent=2)

def timed(fn, *a, **kw):
    t0 = time.time()
    r = fn(*a, **kw)
    t1 = time.time()
    return r, t1-t0
