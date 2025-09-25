# Projeto HPC — Processamento Paralelo de Imagens DICOM

## Visão Geral
Pipeline paralelo para anonimização, compressão e cálculo de estatísticas em imagens médicas DICOM usando MPI e OpenMP.

## Requisitos
- Python 3.10+
- pydicom, numpy, Pillow, mpi4py
- GCC com OpenMP
- SLURM (para execução no Santos Dumont)

## Como Rodar Localmente
```bash
bash scripts/build.sh
bash scripts/run_local.sh
