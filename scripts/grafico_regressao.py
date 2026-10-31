"""Regressão linear simples: gasto mensal em função da renda mensal."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
ARQUIVO_DADOS = RAIZ / "dados" / "dados_regressao.csv"
ARQUIVO_SAIDA = RAIZ / "graficos" / "grafico_regressao.png"


def main():
    df = pd.read_csv(ARQUIVO_DADOS)
    renda = df["renda_mensal"].to_numpy()
    gasto = df["gasto_mensal"].to_numpy()

    # ajuste y = a*x + b e coeficiente de determinação (R²)
    a, b = np.polyfit(renda, gasto, deg=1)
    previsto = a * renda + b
    r2 = 1 - np.sum((gasto - previsto) ** 2) / np.sum((gasto - gasto.mean()) ** 2)

    xs = np.linspace(renda.min(), renda.max(), 200)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(renda, gasto, color="#8d99ae", edgecolor="white", s=55, label="Observações")
    ax.plot(xs, a * xs + b, color="#d00000", linewidth=2.5,
            label=f"Reta ajustada: y = {a:.2f}x + {b:.0f}  (R² = {r2:.3f})")

    ax.set_title("Relação entre renda e gasto mensal", fontsize=14)
    ax.set_xlabel("Renda mensal (R$)")
    ax.set_ylabel("Gasto mensal (R$)")
    ax.legend(loc="upper left")
    ax.grid(linestyle=":", alpha=0.5)

    fig.tight_layout()
    ARQUIVO_SAIDA.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(ARQUIVO_SAIDA, dpi=150)
    plt.show()


if __name__ == "__main__":
    main()
