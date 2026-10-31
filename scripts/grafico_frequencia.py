"""Gráfico de frequência (barras horizontais): chamados por tipo de atendimento."""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
ARQUIVO_DADOS = RAIZ / "dados" / "dados_frequencia.csv"
ARQUIVO_SAIDA = RAIZ / "graficos" / "grafico_frequencia.png"


def main():
    df = pd.read_csv(ARQUIVO_DADOS)
    contagem = df["tipo_atendimento"].value_counts().sort_values()  # menor -> maior
    total = contagem.sum()

    fig, ax = plt.subplots(figsize=(9, 6))
    barras = ax.barh(contagem.index, contagem.values, color="#3a86a8")

    # rótulo com quantidade e percentual no fim de cada barra
    rotulos = [f"{v}  ({v / total:.1%})" for v in contagem.values]
    ax.bar_label(barras, labels=rotulos, padding=4)

    ax.set_xlim(0, contagem.max() * 1.2)
    ax.set_title("Chamados por tipo de atendimento", fontsize=14)
    ax.set_xlabel("Quantidade de chamados")
    ax.set_ylabel("Tipo de atendimento")
    ax.spines[["top", "right"]].set_visible(False)

    fig.tight_layout()
    ARQUIVO_SAIDA.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(ARQUIVO_SAIDA, dpi=150)
    plt.show()


if __name__ == "__main__":
    main()
