#!/usr/bin/env bash
set -e
# exemplo simples de perfilamento de tempo usando /usr/bin/time
/usr/bin/time -v mpirun -np 4 python3 src/main.py --input data_sample/graph_sample.edgelist --metric centrality 2>&1 | tee results/profile.txt
