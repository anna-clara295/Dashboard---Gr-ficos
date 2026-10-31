"""Gráfico de linhas: evolução das vendas de cada loja ao longo do tempo."""
from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
ARQUIVO_DADOS = RAIZ / "dados" / "dados_linhas.csv"
ARQUIVO_SAIDA = RAIZ / "graficos" / "grafico_linhas.png"

CORES = {"Loja A": "#0b6e4f", "Loja B": "#d1495b"}


def main():
    df = pd.read_csv(ARQUIVO_DADOS, parse_dates=["data"]).sort_values("data")

    fig, ax = plt.subplots(figsize=(11, 6))
    for loja, grupo in df.groupby("loja"):
        cor = CORES.get(loja)
        # pontos originais (suaves) + média móvel de 5 registros (linha forte)
        ax.plot(grupo["data"], grupo["vendas"], color=cor, alpha=0.3, marker="o", markersize=3)
        ax.plot(grupo["data"], grupo["vendas"].rolling(5, min_periods=1).mean(),
                color=cor, linewidth=2.5, label=f"{loja} (média móvel)")

    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b/%Y"))
    ax.set_title("Evolução das vendas por loja", fontsize=14)
    ax.set_xlabel("Data")
    ax.set_ylabel("Vendas")
    ax.legend(title="Loja")
    ax.grid(axis="y", linestyle="--", alpha=0.4)
    ax.spines[["top", "right"]].set_visible(False)

    fig.tight_layout()
    ARQUIVO_SAIDA.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(ARQUIVO_SAIDA, dpi=150)
    plt.show()


if __name__ == "__main__":
    main()
