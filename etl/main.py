# %%
import pandas as pd

# Leituras do DataFrames
df_final = pd.DataFrame()
df_order = pd.read_excel('dataset/Sales Report.xls', sheet_name='Orders')

df_people = pd.read_excel('dataset/Sales Report.xls', sheet_name='People')

df_final = pd.merge(df_order, df_people, how='left', on='Region') 

df_final['Ship Days'] = (df_final['Ship Date'] - df_final['Order Date']).dt.days

df_final['Order Month'] = df_final['Order Date'].dt.to_period("M").astype(str)

# Tranformação nas Colunas de Data
df_final['Order Date'] = pd.to_datetime(df_final['Order Date']).dt.date
df_final['Ship Date'] = pd.to_datetime(df_final['Ship Date']).dt.date
# Tranformação da coluna em Int
df_final['Postal Code'] = df_final['Postal Code'].astype("Int64")

# Arredondamento
df_final['Sales'] = df_final['Sales'].round(2)
df_final['Profit'] = df_final['Profit'].round(2)

# Remover as duplicadas
df_final = df_final.drop_duplicates(subset=['Order ID', 'Product ID', 'Order Date'])

# Sumarização
sumary_month = (
    df_final.groupby('Order Month')
    .agg(
        total_sales=('Sales', 'sum'),
        total_profit=('Profit', 'sum'),
        total_order=('Order ID', 'count')
    )
    .round(2)
    .reset_index()
)

summary_region_category = (
    df_final
    .groupby(['Region', 'Category'])
    .agg(
        total_sales=('Sales', 'sum'),
        total_profit=('Profit', 'sum'),
        total_order=('Order ID', 'count')
    )
    .round(2)
    .reset_index()
)

summary_state = (
    df_final
    .groupby(['State'])
    .agg(
        total_sales=('Sales', 'sum'),
        total_profit=('Profit', 'sum'),
        total_order=('Order ID', 'count')
    )
    .round(2)
    .reset_index()
)

summary_segment = (
    df_final
    .groupby(['Segment'])
    .agg(
        total_sales=('Sales', 'sum'),
        total_profit=('Profit', 'sum'),
        total_order=('Order ID', 'count')
    )
    .round(2)
    .reset_index()
)

df_final.to_csv("dataset/processado/df_final.csv")

sumary_month.to_csv("dataset/processado/summary_month.csv")

summary_region_category.to_csv("dataset/processado/summary_region_category.csv")

