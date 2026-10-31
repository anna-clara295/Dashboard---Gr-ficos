"""Histograma com curva de densidade: idade dos clientes."""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

RAIZ = Path(__file__).resolve().parent.parent
ARQUIVO_DADOS = RAIZ / "dados" / "dados_distribuicao.csv"
ARQUIVO_SAIDA = RAIZ / "graficos" / "grafico_distribuicao.png"


def main():
    idades = pd.read_csv(ARQUIVO_DADOS)["idade"].dropna()
    media = idades.mean()
    mediana = idades.median()

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(idades, bins=12, kde=True, color="#6a4c93", edgecolor="white", ax=ax)

    ax.axvline(media, color="#ff595e", linestyle="--", label=f"Média: {media:.1f}")
    ax.axvline(mediana, color="#1982c4", linestyle="-.", label=f"Mediana: {mediana:.1f}")

    ax.set_title("Distribuição da idade dos clientes", fontsize=14)
    ax.set_xlabel("Idade (anos)")
    ax.set_ylabel("Número de clientes")
    ax.legend()
    sns.despine(ax=ax)

    fig.tight_layout()
    ARQUIVO_SAIDA.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(ARQUIVO_SAIDA, dpi=150)
    plt.show()


if __name__ == "__main__":
    main()
