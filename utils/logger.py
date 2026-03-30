import logging

logging.basicConfig(
    filename="execution.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def log_inicio(algoritmo, tamanho):
    logging.info(f"INICIO | Algoritmo: {algoritmo} | Tamanho: {tamanho}")

def log_fim(algoritmo, tempo):
    logging.info(f"FIM | Algoritmo: {algoritmo} | Tempo: {tempo:.6f}s")