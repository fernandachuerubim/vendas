# Projeto de Análise e Previsão de Vendas

Aplicação em Python para análise de dados de vendas, visualização de indicadores e previsão de lucro de produtos. O projeto utiliza Streamlit para a interface web, pandas para processamento dos dados e scikit-learn para o modelo de machine learning.

## Funcionalidades

- Dashboard de vendas e performance com indicadores gerais.
- Análise mensal de vendas, lucro e quantidade de pedidos.
- Visualização de vendas por região e categoria.
- Previsão de lucro utilizando um modelo `RandomForestRegressor`.
- Explicação da previsão por meio de gráfico SHAP waterfall.
- ETL para limpar, transformar e agregar os dados de vendas.
- Notebooks para reprodução da análise, criação do modelo e cálculo de score.

## Tecnologias

- Python 3.13
- Streamlit
- pandas
- Plotly
- scikit-learn
- SHAP
- Joblib
- Jupyter/IPython
- uv

As dependências estão definidas em `pyproject.toml` e bloqueadas em `uv.lock`.

## Estrutura do projeto

```text
.
├── home.py
├── pages/
│   ├── dashboard.py
│   ├── previsao.py
│   └── otimizacao.py
├── etl/
│   └── main.py
├── dataset/
│   ├── Sales Report.xls
│   └── processado/
│       ├── df_final.csv
│       ├── summary_month.csv
│       ├── summary_region_category.csv
│       └── product_agg.csv
├── modelo/
│   └── modelo.joblib
├── notebook/
│   ├── previsao.ipynb
│   └── score.ipynb
├── pyproject.toml
├── uv.lock
└── README.md
```

## Instalação

É necessário ter Python 3.13 e o `uv` instalados.

```bash
uv sync
```

Esse comando cria o ambiente virtual e instala as dependências declaradas no projeto.

## Execução da aplicação

Na raiz do projeto, execute:

```bash
streamlit run home.py
```

A aplicação será aberta no navegador. A navegação atual disponibiliza:

- **Dashboard de Análise de Vendas**: indicadores, gráficos mensais, regionais e por categoria.
- **Machine Learning**: formulário para inserir características de um produto e obter a previsão de lucro.


## Processamento dos dados

O ETL está em `etl/main.py`. Ele lê as abas `Orders` e `People` do arquivo `dataset/Sales Report.xls`, realiza o merge por `Region`, calcula o prazo de entrega em dias, padroniza datas e código postal, remove duplicatas e gera arquivos agregados.

Para reprocessar os dados:

```bash
uv run python etl/main.py
```

Os principais arquivos gerados são:

- `dataset/processado/df_final.csv`: dados tratados em nível de pedido/produto.
- `dataset/processado/summary_month.csv`: totais mensais de vendas, lucro e pedidos.
- `dataset/processado/summary_region_category.csv`: totais por região e categoria.

> Antes de reprocessar os dados, confira os caminhos usados em `etl/main.py`. O arquivo contém uma referência absoluta a `/dataset/Sales Report.xls` que pode precisar ser ajustada para o diretório do projeto.

## Notebooks

Os notebooks permitem reproduzir e estudar as etapas analíticas:

- `notebook/previsao.ipynb`: preparação dos dados, treinamento e avaliação do modelo de previsão.
- `notebook/score.ipynb`: análise e cálculo de indicadores de score dos produtos.

## Arquivo do modelo

O modelo treinado está armazenado em `modelo/modelo.joblib`. A página de previsão carrega esse arquivo e espera as seguintes variáveis:

- categoria;
- subcategoria;
- segmento;
- estado;
- preço;
- quantidade;
- desconto.

## Conclusão

O projeto reúne um fluxo completo de análise de vendas: o ETL trata e agrega os dados da planilha original, os arquivos processados alimentam o dashboard e a análise de portfólio, e o modelo treinado permite estimar o lucro de produtos com base nas variáveis disponíveis. A documentação e os notebooks mantêm registradas as etapas de instalação, execução, processamento, análise e previsão.