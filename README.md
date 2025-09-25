# Projeto HPC — Grafos Municipais (análise de centralidade, comunidades e simulação de falhas)

## Visão geral
Este projeto implementa uma pipeline paralela para análise de grafos representando redes municipais (TI, serviços, ou infraestrutura). O foco é medir escalabilidade e overheads de I/O/communicação ao calcular métricas como centralidade, detecção de comunidades e simulação de remoção de nós (falhas).

## Requisitos
- Python 3.10+
- mpi4py, networkx, numpy, matplotlib
- SLURM e mpirun/mpiexec no cluster Santos Dumont para submissão real

## Como rodar (local / prova de conceito)
1. Instale dependências (recomendado em venv/conda):
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r env/requirements.txt
```

2. Gerar grafo de exemplo:
```bash
python src/generate_graph.py --nodes 1000 --prob 0.01 --out data_sample/graph_sample.edgelist
```

3. Teste local com MPI:
```bash
mpirun -np 4 python3 src/main.py --input data_sample/graph_sample.edgelist --metric centrality
```

## Como rodar no Santos Dumont (resumo)
- Ajuste módulos no script `scripts/job_cpu.slurm`
- Submeta: `sbatch scripts/job_cpu.slurm`
- Monitore: `squeue -u $USER` e logs em `results/`

## Estrutura
(ver árvore no repositório raíz)

## Resultados
Tabelas e gráficos gerados no diretório `results/`.

