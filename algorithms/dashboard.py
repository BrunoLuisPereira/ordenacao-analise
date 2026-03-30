import json
import time
import streamlit as st
from algorithms.insertion_sort import insertion_sort
from algorithms.merge_sort import merge_sort


def medir_tempo(algoritmo, dados):
    dados_copia = dados.copy()
    inicio = time.time()
    algoritmo(dados_copia)
    fim = time.time()
    return fim - inicio


def carregar_dados():
    with open("data/datasets.json", "r") as f:
        return json.load(f)


st.title("📊 Análise de Algoritmos de Ordenação")

datasets = carregar_dados()

tamanhos = []
tempos_insertion = []
tempos_merge = []

for tamanho, dados in datasets.items():
    tamanho_int = int(tamanho)
    tamanhos.append(tamanho_int)

    tempos_insertion.append(medir_tempo(insertion_sort, dados))
    tempos_merge.append(medir_tempo(merge_sort, dados))

st.subheader("Tempo de Execução dos Algoritmos")

st.line_chart({
    "Insertion Sort": tempos_insertion,
    "Merge Sort": tempos_merge
})

st.write("Tamanhos analisados:", tamanhos)