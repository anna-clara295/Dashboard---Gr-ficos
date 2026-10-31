"""Boxplot: distribuição dos salários em cada departamento."""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

RAIZ = Path(__file__).resolve().parent.parent
ARQUIVO_DADOS = RAIZ / "dados" / "dados_boxplot.csv"
ARQUIVO_SAIDA = RAIZ / "graficos" / "grafico_boxplot.png"


def main():
    df = pd.read_csv(ARQUIVO_DADOS)

    # departamentos ordenados pela mediana salarial (do menor para o maior)
    ordem = df.groupby("departamento")["salario"].median().sort_values().index.tolist()

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=df, x="departamento", y="salario", order=ordem,
                hue="departamento", palette="Set2", legend=False,
                showmeans=True,
                meanprops={"marker": "D", "markerfacecolor": "white",
                           "markeredgecolor": "black"},
                ax=ax)

    ax.set_title("Salários por departamento (losango = média)", fontsize=14)
    ax.set_xlabel("Departamento")
    ax.set_ylabel("Salário (R$)")
    ax.yaxis.grid(True, linestyle=":", alpha=0.5)
    ax.set_axisbelow(True)

    fig.tight_layout()
    ARQUIVO_SAIDA.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(ARQUIVO_SAIDA, dpi=150)
    plt.show()


if __name__ == "__main__":
    main()
