import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="Cotação de Moedas - BrasilAPI", layout="wide")

st.title("💱 Cotação de Moedas - Dados via BrasilAPI")

st.markdown("""
Esta aplicação consome dados da [BrasilAPI](https://brasilapi.com.br) para exibir as **cotações de moedas estrangeiras** em relação ao **Real (R$)**.

### Informações exibidas:
- Nome da moeda
- Código da moeda
- Valor atual em R$
- Fonte dos dados
""")

# Endpoint correto da API
url = "https://brasilapi.com.br/api/currency/v1"

try:
    resposta = requests.get(url)
    resposta.raise_for_status()  # Gera exceção se houver erro

    dados = resposta.json()

    if isinstance(dados, list) and len(dados) > 0:
        df = pd.DataFrame(dados)

        # Verifica se as colunas necessárias estão presentes
        if all(col in df.columns for col in ["name", "code", "value", "source"]):
            df = df[["name", "code", "value", "source"]]
            df.columns = ["Nome da Moeda", "Código", "Valor Atual (R$)", "Fonte"]

            # Formatação do valor
            df["Valor Atual (R$)"] = df["Valor Atual (R$)"].apply(lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

            st.markdown("### 📊 Tabela de Cotações")
            st.dataframe(df, use_container_width=True)
        else:
            st.warning("A resposta da API não contém os dados esperados.")
    else:
        st.warning("Nenhum dado encontrado na resposta da API.")


