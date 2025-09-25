#!/usr/bin/env bash
set -e

echo "=== Perfilamento do Projeto HPC ==="

# Perfilamento básico com time
echo "1. Executando versão MPI com profiling..."
time mpirun -np 4 python src/main_mpi.py

echo "2. Executando versão OpenMP com profiling..."
time ./bin/main_omp

echo "3. Verificando uso de memória..."
# Instale se necessário: pip install memory_profiler
python -m memory_profiler src/main_mpi.py

echo "Perfilamento concluído."
