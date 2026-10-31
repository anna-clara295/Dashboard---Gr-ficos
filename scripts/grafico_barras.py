"""Gráfico de barras agrupadas: vendas médias por categoria e região."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
ARQUIVO_DADOS = RAIZ / "dados" / "dados_barras.csv"
ARQUIVO_SAIDA = RAIZ / "graficos" / "grafico_barras.png"


def main():
    df = pd.read_csv(ARQUIVO_DADOS)
    tabela = df.pivot_table(index="categoria", columns="regiao", values="vendas_medias")

    categorias = tabela.index.tolist()
    regioes = tabela.columns.tolist()
    posicoes = np.arange(len(categorias))
    largura = 0.8 / len(regioes)
    cores = ["#264653", "#2a9d8f", "#e9c46a", "#e76f51"]

    fig, ax = plt.subplots(figsize=(11, 6))
    for i, regiao in enumerate(regioes):
        deslocamento = (i - (len(regioes) - 1) / 2) * largura
        barras = ax.bar(posicoes + deslocamento, tabela[regiao], largura,
                        label=regiao, color=cores[i % len(cores)])
        ax.bar_label(barras, fmt="%.0f", fontsize=8, padding=2)

    ax.set_xticks(posicoes)
    ax.set_xticklabels(categorias)
    ax.set_title("Vendas médias por categoria de produto e região", fontsize=14)
    ax.set_xlabel("Categoria de produto")
    ax.set_ylabel("Vendas médias")
    ax.legend(title="Região", frameon=False)
    ax.spines[["top", "right"]].set_visible(False)
    ax.yaxis.grid(True, linestyle="--", alpha=0.4)
    ax.set_axisbelow(True)

    fig.tight_layout()
    ARQUIVO_SAIDA.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(ARQUIVO_SAIDA, dpi=150)
    plt.show()


if __name__ == "__main__":
    main()
