"""Mapa de calor: movimento de clientes por dia da semana e horário."""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

RAIZ = Path(__file__).resolve().parent.parent
ARQUIVO_DADOS = RAIZ / "dados" / "dados_heatmap.csv"
ARQUIVO_SAIDA = RAIZ / "graficos" / "grafico_heatmap.png"

DIAS = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]


def main():
    df = pd.read_csv(ARQUIVO_DADOS)
    matriz = df.pivot_table(index="dia_semana", columns="horario",
                            values="movimento_clientes", aggfunc="mean")
    matriz = matriz.reindex(DIAS)

    fig, ax = plt.subplots(figsize=(11, 6))
    sns.heatmap(matriz, annot=True, fmt=".0f", cmap="Blues",
                linewidths=0.5, linecolor="white",
                cbar_kws={"label": "Clientes"}, ax=ax)

    ax.set_title("Fluxo de clientes por dia e horário", fontsize=14)
    ax.set_xlabel("Horário")
    ax.set_ylabel("Dia da semana")
    plt.setp(ax.get_yticklabels(), rotation=0)

    fig.tight_layout()
    ARQUIVO_SAIDA.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(ARQUIVO_SAIDA, dpi=150)
    plt.show()


if __name__ == "__main__":
    main()
