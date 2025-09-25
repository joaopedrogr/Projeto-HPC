#!/usr/bin/env bash
set -e

# Teste MPI
mpirun -np 4 python src/main_mpi.py

# Teste OpenMP
./bin/main_omp
