#!/usr/bin/env bash
set -e

echo "=== Validação do Projeto HPC ==="

# Verificar estrutura de diretórios
echo "1. Verificando estrutura..."
[ -d "src" ] || { echo "ERRO: Pasta src não encontrada"; exit 1; }
[ -d "scripts" ] || { echo "ERRO: Pasta scripts não encontrada"; exit 1; }

# Verificar arquivos essenciais
echo "2. Verificando arquivos..."
[ -f "src/main_mpi.py" ] || { echo "ERRO: main_mpi.py não encontrado"; exit 1; }
[ -f "scripts/build.sh" ] || { echo "ERRO: build.sh não encontrado"; exit 1; }

# Testar build
echo "3. Testando build..."
bash scripts/build.sh

# Gerar dados de teste
echo "4. Gerando dados de teste..."
python data_sample/generate_sample.py

# Teste rápido
echo "5. Teste rápido de execução..."
mpirun -np 2 python src/main_mpi.py

echo "✅ Validação concluída com sucesso!"
