#!/bin/bash
#SBATCH --job-name=grafos_cpu
#SBATCH --output=results/%x_%j.out
#SBATCH --error=results/%x_%j.err
#SBATCH --time=00:10:00
#SBATCH --ntasks=8
#SBATCH --cpus-per-task=1
#SBATCH --mem=8G

module load python/3.10 mpi
srun python3 src/main.py --input data_sample/graph_sample.edgelist --metric centrality
