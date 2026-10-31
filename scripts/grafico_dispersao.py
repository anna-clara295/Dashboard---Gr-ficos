"""Gráfico de dispersão: altura x peso, separado por sexo."""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

RAIZ = Path(__file__).resolve().parent.parent
ARQUIVO_DADOS = RAIZ / "dados" / "dados_dispersao.csv"
ARQUIVO_SAIDA = RAIZ / "graficos" / "grafico_dispersao.png"


def main():
    df = pd.read_csv(ARQUIVO_DADOS).drop_duplicates()

    fig, ax = plt.subplots(figsize=(9, 6))
    sns.scatterplot(data=df, x="altura_cm", y="peso_kg", hue="sexo",
                    style="sexo", palette={"Feminino": "#d62728", "Masculino": "#1f77b4"},
                    s=70, alpha=0.8, ax=ax)

    ax.set_title("Altura e peso por sexo", fontsize=14)
    ax.set_xlabel("Altura (cm)")
    ax.set_ylabel("Peso (kg)")
    ax.legend(title="Sexo", loc="upper left")
    sns.despine(ax=ax)

    fig.tight_layout()
    ARQUIVO_SAIDA.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(ARQUIVO_SAIDA, dpi=150)
    plt.show()


if __name__ == "__main__":
    main()
