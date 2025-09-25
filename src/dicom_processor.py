import pydicom
import numpy as np
import os
from PIL import Image

def anonymize_dicom(ds):
    """Remove informações sensíveis do arquivo DICOM"""
    tags_to_remove = [
        (0x0010, 0x0010),  # PatientName
        (0x0010, 0x0020),  # PatientID
        (0x0010, 0x0030),  # PatientBirthDate
        (0x0010, 0x0040),  # PatientSex
    ]
    for tag in tags_to_remove:
        if tag in ds:
            del ds[tag]
    return ds

def compress_image(pixel_array, format='JPEG', quality=85):
    """Comprime o array de pixels para JPEG"""
    img = Image.fromarray(pixel_array.astype(np.uint8))
    # Simulação de compressão
    return img

def compute_stats(pixel_array):
    """Calcula estatísticas da imagem"""
    return {
        'min': np.min(pixel_array),
        'max': np.max(pixel_array),
        'mean': np.mean(pixel_array),
        'std': np.std(pixel_array)
    }
