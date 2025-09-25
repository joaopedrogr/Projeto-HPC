import numpy as np
from PIL import Image
import pydicom
import json
import os

def generate_sample_dicom(output_dir, num_files=10):
    """Gera arquivos DICOM sintéticos para testes"""
    os.makedirs(output_dir, exist_ok=True)
    
    for i in range(num_files):
        # Cria array de pixels sintético (512x512)
        pixel_array = np.random.randint(0, 255, (512, 512), dtype=np.uint16)
        
        # Cria dataset DICOM básico
        ds = pydicom.Dataset()
        ds.PatientName = f"Patient_{i}"
        ds.PatientID = f"ID_{i:06d}"
        ds.StudyDescription = "Sample Study"
        ds.Rows = 512
        ds.Columns = 512
        ds.PixelData = pixel_array.tobytes()
        ds.PhotometricInterpretation = "MONOCHROME2"
        ds.SamplesPerPixel = 1
        ds.BitsStored = 16
        ds.BitsAllocated = 16
        ds.HighBit = 15
        ds.PixelRepresentation = 0
        
        # Salva arquivo
        filename = os.path.join(output_dir, f"sample_{i:03d}.dcm")
        ds.save_as(filename)
        print(f"Gerado: {filename}")

def save_stats(stats, filename):
    """Salva estatísticas em JSON"""
    with open(filename, 'w') as f:
        json.dump(stats, f, indent=2)

def load_stats(filename):
    """Carrega estatísticas do JSON"""
    with open(filename, 'r') as f:
        return json.load(f)
