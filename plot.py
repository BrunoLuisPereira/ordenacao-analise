import json
import time
import matplotlib.pyplot as plt

from algorithms.insertion_sort import insertion_sort
from algorithms.merge_sort import merge_sort
from algorithms.bubble_sort import bubble_sort


def medir_tempo(algoritmo, dados):
    dados_copia = dados.copy()
    inicio = time.time()
    algoritmo(dados_copia)
    fim = time.time()
    return fim - inicio


def carregar_dados():
    with open("data/datasets.json", "r") as f:
        return json.load(f)


def gerar_grafico():
    datasets = carregar_dados()

    tamanhos = []
    tempos_insertion = []
    tempos_merge = []
    tempos_bubble = []

    for tamanho, dados in datasets.items():
        tamanho_int = int(tamanho)
        tamanhos.append(tamanho_int)

        tempos_insertion.append(medir_tempo(insertion_sort, dados))
        tempos_merge.append(medir_tempo(merge_sort, dados))
        tempos_bubble.append(medir_tempo(bubble_sort, dados))

    plt.plot(tamanhos, tempos_insertion, marker='o', label='Insertion Sort')
    plt.plot(tamanhos, tempos_merge, marker='o', label='Merge Sort')
    plt.plot(tamanhos, tempos_bubble, marker='o', label='Bubble Sort')

    plt.xlabel("Tamanho da Entrada")
    plt.ylabel("Tempo de Execução (s)")
    plt.title("Comparação de Algoritmos de Ordenação")
    plt.legend()
    plt.grid()

    plt.show()


if __name__ == "__main__":
    gerar_grafico()