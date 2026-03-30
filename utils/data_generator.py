import random
import json
import os

def gerar_dados():
    tamanhos = [1000, 5000, 10000, 50000]
    datasets = {}

    for tamanho in tamanhos:
        datasets[str(tamanho)] = [random.randint(0, 100000) for _ in range(tamanho)]

    # garante que a pasta data existe
    os.makedirs("data", exist_ok=True)

    with open("data/datasets.json", "w") as f:
        json.dump(datasets, f)

    print("Dados gerados com sucesso!")

if __name__ == "__main__":
    gerar_dados()