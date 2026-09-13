import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Dashboard de Análises de Vendas e Performance', layout='wide')

st.header('Dashboard de Análise de Vendas e Performance')

@st.cache_data
def load_data(): 
    df = pd.read_csv('dataset/processado/df_final.csv')
    return df

@st.cache_data
def load_data_month():
    df_month = pd.read_csv("dataset/processado/summary_month.csv")
    return df_month

@st.cache_data
def load_region_category():
    df_region = pd.read_csv("dataset/processado/summary_region_category.csv")
    return df_region

df = load_data()
df_month = load_data_month()
df_region = load_region_category()


col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        label='Qtd Vendida',
        value=f"{df['Quantity'].sum() / 1_000:,.0f} mil"
    )

with col2:
    st. metric(
        label='Qtd Pedidos',
        value=f"{df['Order ID'].nunique() / 1_000:,.0f} mil"
    )

with col3:
    st.metric(
        label='Ticket Médio',
        value=f"{df['Sales'].sum() /df['Order ID'].nunique():,.2f}".replace(".", ",")
    )

with col4:
    st.metric(
        label='Faturamento Total',
        value=f"{df['Sales'].sum() / 1_000_000:,.0f} milhões"
    ) 

with col5:
    st.metric(
        label='Margem de Lucro',
        value=f"{df['Profit'].sum()/df['Sales'].sum():.2%}"
    )

fig = px.line(
    df_month,
    x='Order Month',
    y=['total_sales', 'total_profit'],
    title='Vendas e Lucro por Mês',
    labels={"Order Month": "Mês", "value": "Quantidades"}
    )

fig.update_layout(
    title_x=0.4
)

st.plotly_chart(fig)

st.write('As vendas oscilam ao longo do período, mas mostram tendência de crescimento. Os principais picos ocorrem em setembro de 2015, novembro/dezembro de 2016, ' \
'dezembro de 2017 e novembro de 2018, que registra o maior valor da série. O lucro acompanha esse comportamento em menor escala.')

fig = px.line(
    df_month,
    x='Order Month',
    y=['total_order'],
    title='Quantidade de Pedidos por Mês',
    labels={"Order Month": "Mês", "value": "Quantidades"}
    )

fig.update_layout(
    title_x=0.4
)

st.plotly_chart(fig)

st.write('A quantidade de pedidos apresenta tendência de crescimento ao longo do período. Os principais picos ocorrem em novembro de 2015 '
'novembro de 2016, novembro de 2017 e setembro e dezembro de 2018, que registram os maiores volumes da série.')

aux = df_region.groupby("Region").agg(
    sales=('total_sales', 'sum'),
).reset_index()

fig = px.bar(
    data_frame=aux,
    x='Region',
    y=['sales'],
    title='Vendas por Região'
)

fig.update_layout(
    title_x=0.4
)

st.plotly_chart(fig)

st.write('As vendas variam entre as regiões, com destaque para a West, que apresenta o maior volume, com cerca de 720 mil. ' \
'Em seguida aparece a East, com aproximadamente 680 mil, enquanto Central registra cerca de 500 mil e South apresenta o menor resultado, próximo de 390 mil.')

aux = (
    df_region
    .groupby('Category')
    .agg(sales=('total_sales', 'sum'))
    .reset_index()
)

fig = px.pie(
    data_frame=aux,
    values='sales',
    names='Category',
    title='Categoria por Vendas'
)

fig.update_layout(
    title_x=0.4
)

st.plotly_chart(fig)

st.write('As vendas estão bem distribuídas entre as categorias, com destaque para Technology, que lidera com 36,4%. ' \
'Em seguida aparecem Furniture, com 32,3%, e Office Supplies, com 31,3%, mostrando uma participação relativamente equilibrada entre as três categorias.')



