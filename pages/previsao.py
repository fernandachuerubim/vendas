import pandas as pd
import streamlit as st
import joblib
import shap
import matplotlib.pyplot as plt

st.set_page_config(page_title='Machine Learning', layout='wide')

st.header('Machine Learning - Previsão do Lucro dos Produtos')

st.write('Selecione as opções abaixo:')

@st.cache_data # nao carregar toda hora o dataset
def load_data():
    df = pd.read_csv("dataset/processado/df_final.csv")
    return df

df = load_data()

# st.dataframe(df)

df.columns = (df.columns
            .str.lower()
            .str.replace(" ","_")
            .str.replace("-", "_")
)

with st.form('previsao'):

    categoria = st.selectbox(
        label='Categoria',
        options=df['category'].unique()
    )

    sub_categoria = st.selectbox(
        label='Sub_Categoria',
        options=df['sub_category'].unique()
    )

    segmento = st.selectbox(
        label='Segment',
        options=df['segment'].unique()
    )

    estado = st.selectbox(
        label='Estado',
        options=df['state'].unique()
    )

    preco = st.slider(
        label='Preço',
        min_value=100,
        max_value=23_000,
    )

    quantidade= st.slider(
        label='Quantidade',
        min_value=1,
        max_value=15
    )

    desconto = st.slider(
        label='Desconto',
        min_value=0.0,
        max_value=0.8,
        format='percent',
    )

    prever = st.form_submit_button('⏳Rodar Previsão 👈 clique aqui', use_container_width=True)

    if prever:

        dados = pd.DataFrame({

            'category': [categoria],

            'sub_category': [sub_categoria],

            'segment': [segmento],

            'state': [estado],

            'sales': [preco],

            'quantity': [quantidade],

            'discount': [desconto],

        })

        modelo = joblib.load('modelo/modelo.joblib') #carrega o modelo

        pred = modelo.predict(dados)

        st.write(f'O modelo Random Forest Regressor estimou um lucro de aproximadamente **{pred[0]:,.2f} U$$** para a combinação informada: categoria **{categoria}** ' \
        f'subcategoria **{sub_categoria}**, segmento **{segmento}**, estado **{estado}**, preço de **{preco}**, quantidade **{quantidade}** e desconto de **{desconto:.0%}**. O resultado representa a previsão de lucro ' \
        f'com base nos padrões aprendidos pelo modelo nos dados históricos.')

        preprocessor = modelo.named_steps['preprocessor']

        rf_model = modelo.named_steps['rf']

        dados_processados = preprocessor.transform(dados)

        cols_name = ['category', 'sub_category', 'segment', 'state', 'sales', 'quantity', 'discount']

        dados_processados_df = pd.DataFrame(
                    dados_processados,
                    columns=cols_name
        )

        explainer = shap.TreeExplainer(rf_model)

        shap_values = explainer(dados_processados_df)

        shap_values.data = dados[cols_name].values

        shap_values.feature_names = [
            'Categoria',
            'Subcategoria',
            'Segmento',
            'Estado',
            'Preço',
            'Quantidade',
            'Desconto'
        ]

        st.subheader('Explicação da previsão')

        fig = plt.figure()

        shap.plots.waterfall(
            shap_values[0],
            show=False
        )

        st.pyplot(fig)

        plt.close(fig)

        st.markdown(
            f"""
            ### Como interpretar o gráfico

            - 🔴 **Vermelho:** aumenta a contribuição para a previsão.

            - 🔵 **Azul:** reduz a contribuição para a previsão.

            - Quanto maior a barra, maior a influência da variável.

            - **base value:** valor médio das previsões do modelo {shap_values.base_values[0]:,.2f}.

            - **f(x):** previsão final para o registro analisado {pred[0]:,.2f} U$$.
            """
        )










