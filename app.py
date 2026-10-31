"""Dashboard em Streamlit com os 9 gráficos da atividade 06.

Como executar (na pasta raiz do projeto):
    streamlit run app.py
"""
from pathlib import Path

import pandas as pd
import streamlit as st

# ----------------------------------------------------------------------
# DADOS DO ALUNO  -> edite aqui com as suas informações
# ----------------------------------------------------------------------
NOME_ALUNO = "Anna Clara Rocha Silva"
NUMERO_CHAMADA = "04"
TURMA = "3D1"

RAIZ = Path(__file__).resolve().parent
PASTA_DADOS = RAIZ / "dados"
PASTA_GRAFICOS = RAIZ / "graficos"


def ler(nome_csv, **kwargs):
    return pd.read_csv(PASTA_DADOS / nome_csv, **kwargs)


def brl(valor):
    """Formata número no padrão brasileiro: 120000 -> 120.000"""
    return f"{valor:,.0f}".replace(",", ".")


# ----------------------------------------------------------------------
# ANÁLISES (calculadas a partir dos próprios CSVs)
# ----------------------------------------------------------------------
def analise_barras():
    df = ler("dados_barras.csv")
    por_regiao = df.groupby("regiao")["vendas_medias"].mean()
    por_cat = df.groupby("categoria")["vendas_medias"].mean()
    maior = df.loc[df["vendas_medias"].idxmax()]
    menor = df.loc[df["vendas_medias"].idxmin()]
    return (
        f"A região **{por_regiao.idxmax()}** tem a maior média de vendas "
        f"({por_regiao.max():.0f}) e a **{por_regiao.idxmin()}** a menor "
        f"({por_regiao.min():.0f}). Entre as categorias, **{por_cat.idxmax()}** "
        f"lidera em média. O maior valor isolado é {maior['categoria']} no "
        f"{maior['regiao']} ({maior['vendas_medias']:.0f}) e o menor é "
        f"{menor['categoria']} no {menor['regiao']} ({menor['vendas_medias']:.0f})."
    )


def analise_boxplot():
    df = ler("dados_boxplot.csv")
    med = df.groupby("departamento")["salario"].median()
    return (
        f"**{med.idxmax()}** tem a maior mediana salarial (R$ {brl(med.max())}) e "
        f"**{med.idxmin()}** a menor (R$ {brl(med.min())}). Os departamentos de "
        f"TI e Vendas pagam bem mais que Marketing e RH, e todos apresentam "
        f"*outliers* (pontos acima da caixa), ou seja, poucos salários muito "
        f"acima do padrão do setor."
    )


def analise_dispersao():
    df = ler("dados_dispersao.csv").drop_duplicates()
    corr = df["altura_cm"].corr(df["peso_kg"])
    medias = df.groupby("sexo")[["altura_cm", "peso_kg"]].mean()
    return (
        f"Há uma correlação positiva forte entre altura e peso "
        f"(r = {corr:.2f}): quanto mais alta a pessoa, maior tende a ser o peso. "
        f"As médias dos dois grupos são parecidas "
        f"(feminino: {medias.loc['Feminino', 'altura_cm']:.1f} cm e "
        f"{medias.loc['Feminino', 'peso_kg']:.1f} kg; masculino: "
        f"{medias.loc['Masculino', 'altura_cm']:.1f} cm e "
        f"{medias.loc['Masculino', 'peso_kg']:.1f} kg), então os pontos se misturam."
    )


def analise_distribuicao():
    idades = ler("dados_distribuicao.csv")["idade"]
    return (
        f"A idade média dos clientes é {idades.mean():.1f} anos e a mediana é "
        f"{idades.median():.0f}. Como a média fica acima da mediana, a "
        f"distribuição é assimétrica à direita: {(idades <= 30).mean():.0%} dos "
        f"clientes têm até 30 anos, e há poucos acima de 55 "
        f"(máximo de {idades.max()} anos)."
    )


def analise_frequencia():
    freq = ler("dados_frequencia.csv")["tipo_atendimento"].value_counts()
    total = freq.sum()
    return (
        f"Dos {total} chamados, **{freq.index[0]}** é o tipo mais comum "
        f"({freq.iloc[0]}, {freq.iloc[0] / total:.1%}), seguido de "
        f"{freq.index[1]} ({freq.iloc[1] / total:.1%}). **{freq.index[-1]}** é o "
        f"menos frequente ({freq.iloc[-1] / total:.1%}). Dúvidas e reclamações "
        f"juntas somam {(freq.iloc[0] + freq.iloc[1]) / total:.0%} do total."
    )


def analise_heatmap():
    df = ler("dados_heatmap.csv")
    pico = df.loc[df["movimento_clientes"].idxmax()]
    por_dia = df.groupby("dia_semana")["movimento_clientes"].mean()
    return (
        f"O maior movimento ocorre no(a) **{pico['dia_semana']} às "
        f"{pico['horario']}**, com {pico['movimento_clientes']} clientes. "
        f"Os fins de semana concentram o fluxo: {por_dia.idxmax()} tem a maior "
        f"média diária ({por_dia.max():.0f}) e {por_dia.idxmin()} a menor "
        f"({por_dia.min():.0f}). Nos dias úteis o movimento é mais baixo e disperso."
    )


def analise_linhas():
    df = ler("dados_linhas.csv", parse_dates=["data"]).sort_values("data")
    medias = df.groupby("loja")["vendas"].mean()
    inicio = df.head(10)["vendas"].mean()
    fim = df.tail(10)["vendas"].mean()
    return (
        f"As vendas das duas lojas crescem ao longo do período "
        f"({df['data'].min():%d/%m} a {df['data'].max():%d/%m/%Y}): a média dos "
        f"10 primeiros registros é {inicio:.0f} e a dos 10 últimos é {fim:.0f} "
        f"(alta de {fim / inicio - 1:.0%}). A **{medias.idxmax()}** tem a maior "
        f"média de vendas ({medias.max():.1f}), mas as curvas andam muito próximas."
    )


def analise_pizza():
    df = ler("dados_pizza.csv").sort_values("faturamento", ascending=False)
    total = df["faturamento"].sum()
    top = df.iloc[0]
    dois = df.head(2)["faturamento"].sum() / total
    return (
        f"O faturamento total é de R$ {brl(total)}. O canal **{top['canal_venda']}** "
        f"é o principal, com {top['faturamento'] / total:.1%} do total. "
        f"Os dois maiores canais ({df.iloc[0]['canal_venda']} e "
        f"{df.iloc[1]['canal_venda']}) juntos respondem por {dois:.0%}, enquanto "
        f"**{df.iloc[-1]['canal_venda']}** tem a menor participação "
        f"({df.iloc[-1]['faturamento'] / total:.1%})."
    )


def analise_regressao():
    df = ler("dados_regressao.csv")
    corr = df["renda_mensal"].corr(df["gasto_mensal"])
    proporcao = (df["gasto_mensal"] / df["renda_mensal"]).mean()
    return (
        f"Renda e gasto têm correlação positiva muito forte (r = {corr:.2f}, "
        f"R² = {corr ** 2:.2f}): a reta explica quase toda a variação do gasto. "
        f"Em média, as pessoas gastam cerca de {proporcao:.0%} da renda mensal, "
        f"e o gasto sobe de forma praticamente linear conforme a renda aumenta."
    )


# (título, arquivo da imagem, função que gera a análise) — 3 por linha
GRAFICOS = [
    ("Barras: vendas por categoria e região", "grafico_barras.png", analise_barras),
    ("Boxplot: salários por departamento", "grafico_boxplot.png", analise_boxplot),
    ("Dispersão: altura × peso", "grafico_dispersao.png", analise_dispersao),
    ("Distribuição: idade dos clientes", "grafico_distribuicao.png", analise_distribuicao),
    ("Frequência: tipos de atendimento", "grafico_frequencia.png", analise_frequencia),
    ("Heatmap: movimento de clientes", "grafico_heatmap.png", analise_heatmap),
    ("Linhas: vendas ao longo do tempo", "grafico_linhas.png", analise_linhas),
    ("Pizza: faturamento por canal", "grafico_pizza.png", analise_pizza),
    ("Regressão: renda × gasto", "grafico_regressao.png", analise_regressao),
]


def main():
    st.set_page_config(
        page_title="Dashboard de Gráficos",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded",  # o sidebar pode ser recolhido pela seta
    )

    # ---------------- Sidebar (recolhível) com dados do aluno ----------------
    with st.sidebar:
        st.header("👤 Informações do aluno")
        st.markdown(f"**Nome:** {NOME_ALUNO}")
        st.markdown(f"**Nº da chamada:** {NUMERO_CHAMADA}")
        st.markdown(f"**Turma:** {TURMA}")
        st.divider()
        st.caption("Atividade 07 · Dashboard com Streamlit")

    # ---------------- Corpo da página ----------------
    st.title("📊 Dashboard de Gráficos")
    st.write("Visualização dos 9 gráficos gerados na atividade 06, com uma breve "
             "análise dos dados abaixo de cada linha.")

    # percorre a lista de 3 em 3
    for inicio in range(0, len(GRAFICOS), 3):
        linha = GRAFICOS[inicio:inicio + 3]

        # 1) três gráficos lado a lado
        colunas_img = st.columns(3)
        for coluna, (titulo, arquivo, _) in zip(colunas_img, linha):
            with coluna:
                st.subheader(titulo)
                st.image(str(PASTA_GRAFICOS / arquivo), use_container_width=True)

        # 2) análises logo abaixo, alinhadas a cada gráfico
        colunas_txt = st.columns(3)
        for coluna, (_, _, gerar_analise) in zip(colunas_txt, linha):
            with coluna:
                st.info(gerar_analise())

        st.divider()


if __name__ == "__main__":
    main()
