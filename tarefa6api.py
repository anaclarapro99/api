

import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Cotação de Moedas - BrasilAPI", layout="wide")

st.title("💱 Cotação de Moedas - Dados via BrasilAPI")

st.markdown("""
Esta aplicação consome dados da [BrasilAPI](https://brasilapi.com.br) para exibir as **cotações de moedas estrangeiras** em relação ao **Real (R$)**.

Abaixo estão listadas as moedas disponíveis com:
- Nome da moeda
- Código da moeda
- Valor atual em R$
- Fonte dos dados
""")

# Chamada da API
url = "https://brasilapi.com.br/api/currency/v1"
resposta = requests.get(url)

if resposta.status_code == 200:
    dados = resposta.json()
    df = pd.DataFrame(dados)
    df = df[["name", "code", "value", "source"]]
    df.columns = ["Nome da Moeda", "Código", "Valor em R$", "Fonte"]

    st.dataframe(df, use_container_width=True)
else:
    st.error("Erro ao buscar dados da API. Tente novamente mais tarde.")
