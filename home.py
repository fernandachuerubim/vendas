import streamlit as st

score = st.Page(
    "pages/dashboard.py", title="Dashboard de Análise de Vendas"
)

otimizacao = st.Page(
    "pages/otimizacao.py", title="Otimização de Portfólio de Produtos"
)

previsao = st.Page(
    "pages/previsao.py", title="Machine Learning"
)

if __name__ == "__main__":
    pg = st.navigation([score, previsao])
    pg.run()















