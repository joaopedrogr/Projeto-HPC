#!/usr/bin/env bash
set -e
# runs a small local mpi test with 4 processes (machine must support mpirun)
mpirun -np 4 python3 src/main.py --input data_sample/graph_sample.edgelist --metric centrality
