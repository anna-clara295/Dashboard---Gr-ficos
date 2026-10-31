"""Gráfico de pizza (formato rosca): participação de cada canal no faturamento."""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
ARQUIVO_DADOS = RAIZ / "dados" / "dados_pizza.csv"
ARQUIVO_SAIDA = RAIZ / "graficos" / "grafico_pizza.png"


def main():
    df = pd.read_csv(ARQUIVO_DADOS).sort_values("faturamento", ascending=False)
    total = df["faturamento"].sum()

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(df["faturamento"],
           autopct="%1.1f%%", pctdistance=0.78, startangle=140, counterclock=False,
           colors=plt.cm.Set3.colors[:len(df)],
           wedgeprops={"width": 0.45, "edgecolor": "white", "linewidth": 2})

    ax.text(0, 0, f"Total\nR$ {total:,.0f}".replace(",", "."),
            ha="center", va="center", fontsize=14, fontweight="bold")
    ax.legend(df["canal_venda"], title="Canal de venda",
              loc="center left", bbox_to_anchor=(1, 0.5), frameon=False)
    ax.set_title("Faturamento por canal de venda", fontsize=14)

    fig.tight_layout()
    ARQUIVO_SAIDA.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(ARQUIVO_SAIDA, dpi=150, bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    main()
