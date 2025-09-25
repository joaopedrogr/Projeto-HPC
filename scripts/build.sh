#!/usr/bin/env bash
set -e

# Instala dependências Python
pip install -r env/requirements.txt

# Compila OpenMP
gcc -fopenmp -O3 -o bin/main_omp src/main_omp.c

echo "Build concluído."
