#!/bin/bash
#SBATCH --job-name=dicom_gpu
#SBATCH --output=results/%x_%j.out
#SBATCH --error=results/%x_%j.err
#SBATCH --time=00:15:00
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --partition=gpu

echo "Iniciando job GPU em $(date)"
echo "Host: $(hostname)"
echo "GPU: $CUDA_VISIBLE_DEVICES"

# Carregar módulos (ajustar para Santos Dumont)
module load cuda/11.8
module load python/3.10
module load pytorch

# Verificar GPU
nvidia-smi

# Executar (versão GPU futura)
python src/main_gpu.py

echo "Concluído em $(date)"
