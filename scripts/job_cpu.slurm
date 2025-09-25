#!/bin/bash
#SBATCH --job-name=dicom_cpu
#SBATCH --output=results/%x_%j.out
#SBATCH --error=results/%x_%j.err
#SBATCH --time=00:10:00
#SBATCH --ntasks=8
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G
#SBATCH --partition=cpu

module load python/3.10 openmpi
srun python src/main_mpi.py
