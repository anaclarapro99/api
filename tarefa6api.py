

import streamlit as st
import requests

st.set_page_config(page_title="Cotação de Moedas", layout="centered")

st.title("💱 Cotação de Moedas - BrasilAPI")

moedas = ["USD", "EUR", "BTC"]
moeda_escolhida = st.selectbox("Escolha a moeda:", moedas)

url = f"https://brasilapi.com.br/api/currency/v1/{moeda_escolhida}"
resposta = requests.get(url)

if resposta.status_code == 200:
    dados = resposta.json()
    st.metric(label="Nome", value=dados["name"])
    st.metric(label="Código", value=dados["code"])
    st.metric(label="Valor Atual (R$)", value=f'{dados["value"]:.2f}')
    st.metric(label="Fonte", value=dados["source"])
else:
    st.error("Erro ao buscar dados. Tente novamente mais tarde.")

    streamlit
    requests
