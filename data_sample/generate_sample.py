#!/usr/bin/env python3
"""
Script para gerar dados DICOM sintéticos para testes
"""

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from utils import generate_sample_dicom

if __name__ == "__main__":
    output_dir = "data_sample"
    num_files = 20  # Número de arquivos para gerar
    
    print(f"Gerando {num_files} arquivos DICOM sintéticos em {output_dir}/")
    generate_sample_dicom(output_dir, num_files)
    print("Concluído!")
