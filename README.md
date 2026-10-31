# Atividade de gráficos

Projeto com 9 gráficos feitos em Python.

## Como executar

1. Instale as bibliotecas:

   ```bash
   pip install -r requirements.txt
   ```

2. Execute um dos scripts, por exemplo:

   ```bash
   python scripts/grafico_barras.py
   ```

Os dados ficam na pasta `dados`. Os gráficos são salvos na pasta `graficos`.

## Scripts

- `grafico_barras.py`
- `grafico_boxplot.py`
- `grafico_dispersao.py`
- `grafico_distribuicao.py`
- `grafico_frequencia.py`
- `grafico_heatmap.py`
- `grafico_linhas.py`
- `grafico_pizza.py`
- `grafico_regressao.py`

## Dashboard (Streamlit)

O arquivo `app.py` reúne os 9 gráficos em um dashboard, três por linha, com uma breve
análise dos dados abaixo de cada um e um sidebar recolhível com as informações do aluno.

Antes de executar, edite no começo do `app.py` as variáveis `NOME_ALUNO`,
`NUMERO_CHAMADA` e `TURMA`. Depois rode:

```bash
pip install -r requirements.txt
streamlit run app.py
```
