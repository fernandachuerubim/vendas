import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Otimização de Portfólio de Produtos', layout='wide')

st.header('Otimização de Portfólio de Produtos')

@st.cache_data
def load_data():
    df = pd.read_csv('dataset/processado/product_agg.csv')
    return df

df = load_data()

aux = df.sort_values(by='profit', ascending=False).head(10)

fig = px.bar(
    data_frame=aux,
    x='product_name',
    y='profit',
    labels={'product_name': 'Nome do Produto', 'profit': 'Faturamento'},
    title='Faturamento por Produto'
)

fig.update_layout(
    title_x=0.4
)

st.plotly_chart(fig)

aux = df.sort_values(by='growth', ascending=False).head(10)

fig = px.bar(
    data_frame=aux,
    x='product_name',
    y='growth',
    labels={'product_name': 'Nome do Produto', 'growth': 'Variação(%)'},
    title='Variação(%) por Produto'
)

fig.update_layout(
    title_x=0.4
)

st.plotly_chart(fig)

aux = df.sort_values(by='quantity', ascending=False).head(10)

fig = px.bar(
    data_frame=aux,
    x='product_name',
    y='quantity',
    title= 'Produtos mais Vendidos',
    labels={'product_name': 'Nome do Produto', 'quantity': 'Quantidades'}
)

fig.update_layout(
    title_x=0.4
)

st.plotly_chart(fig)

aux = df.sort_values(by='margin', ascending=False).head(10)

fig = px.bar(
    data_frame=aux,
    x='product_name',
    y='margin',
    labels={'product_name': 'Nome do Produto', 'margin': 'Margem'},
    title='Margem dos Produtos'
)

fig.update_layout(
    title_x=0.4
)

st.plotly_chart(fig)

aux = df.sort_values(by='stability_score', ascending=False).head(10)

fig = px.bar(
    data_frame=aux,
    x='product_name',
    y='stability_score',
    labels={'product_name': 'Nome do Produto', 'stability_score': 'score'},
    title='Score dos Produtos'
)

fig.update_layout(
    title_x=0.4
)

st.plotly_chart(fig)




