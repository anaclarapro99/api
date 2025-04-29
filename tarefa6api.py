

import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Cotação de Moedas - BrasilAPI", layout="wide")

# Título e descrição
st.title("💱 Cotação de Moedas - Dados via BrasilAPI")

st.markdown("""
Esta aplicação consome dados da [BrasilAPI](https://brasilapi.com.br) para exibir as **cotações de moedas estrangeiras** em relação ao **Real (R$)**.

### 🧾 Informações exibidas:
- **Nome da moeda**
- **Código da moeda**
- **Valor atual em R$**
- **Fonte dos dados**
""")

# API
url = "https://brasilapi.com.br/api/currency/v1"
resposta = requests.get(url)

if resposta.status_code == 200:
    dados = resposta.json()
    
    # Organizando os dados com Pandas
    df = pd.DataFrame(dados)
    df = df[["name", "code", "value", "source"]]
    df.columns = ["🪙 Nome da Moeda", "Código", "💲 Valor Atual (R$)", "📡 Fonte"]

    # Ordena por nome
    df = df.sort_values(by="🪙 Nome da Moeda")

    # Exibição da tabela estilizada
    st.markdown("### 📊 Tabela de Cotações")
    st.dataframe(df.style.format({"💲 Valor Atual (R$)": "R$ {:.2f}"}), use_container_width=True)


