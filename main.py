import json
import time
from algorithms.insertion_sort import insertion_sort
from algorithms.merge_sort import merge_sort
from algorithms.bubble_sort import bubble_sort
from utils.logger import log_inicio, log_fim


def medir_tempo(algoritmo, dados, nome, tamanho):
    dados_copia = dados.copy()  

    log_inicio(nome, tamanho)

    inicio = time.time()
    algoritmo(dados_copia)
    fim = time.time()

    tempo = fim - inicio

    log_fim(nome, tempo)

    return tempo


def carregar_dados():
    with open("data/datasets.json", "r") as f:
        return json.load(f)


if __name__ == "__main__":
    datasets = carregar_dados()

    for tamanho, dados in datasets.items():
        print(f"\nTamanho: {tamanho}")

        # Insertion Sort
        tempo_insertion = medir_tempo(
            insertion_sort, dados, "Insertion Sort", tamanho
        )
        print(f"Insertion Sort: {tempo_insertion:.6f}s")

        # Merge Sort
        tempo_merge = medir_tempo(
            merge_sort, dados, "Merge Sort", tamanho
        )
        print(f"Merge Sort: {tempo_merge:.6f}s")

        # Bubble Sort
        tempo_bubble = medir_tempo(
            bubble_sort, dados, "Bubble Sort", tamanho
        )
        print(f"Bubble Sort: {tempo_bubble:.6f}s")