from mpi4py import MPI
import os
import time
from dicom_processor import anonymize_dicom, compress_image, compute_stats
import pydicom

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def process_dicom_file(filepath):
    """Processa um arquivo DICOM: anonimiza, comprime, calcula stats"""
    ds = pydicom.dcmread(filepath)
    ds = anonymize_dicom(ds)
    pixel_array = ds.pixel_array
    stats = compute_stats(pixel_array)
    compress_image(pixel_array)  # simulação
    return stats

if __name__ == "__main__":
    data_dir = "data_sample/"
    files = [os.path.join(data_dir, f) for f in os.listdir(data_dir) if f.endswith('.dcm')]
    
    # Distribuição round-robin
    local_files = [f for i, f in enumerate(files) if i % size == rank]
    
    t0 = time.time()
    local_stats = []
    for f in local_files:
        try:
            stats = process_dicom_file(f)
            local_stats.append(stats)
        except Exception as e:
            print(f"Erro em {f}: {e}")
    
    # Coleta estatísticas globais
    all_stats = comm.gather(local_stats, root=0)
    
    if rank == 0:
        total_files = sum(len(stats) for stats in all_stats)
        t1 = time.time()
        print(f"Processados {total_files} arquivos em {t1-t0:.2f}s com {size} processos.")
