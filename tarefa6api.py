import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Cotação de Moedas - BrasilAPI", layout="wide")

st.title("💱 Cotação de Moedas - BrasilAPI")

# Consumir a API
url = "https://brasilapi.com.br/api/currency/v1"
response = requests.get(url)

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    dados = response.json()

    # Extrair os dados principais
    tabela = []
    for moeda in dados:
        tabela.append({
            "Nome": moeda.get("name"),
            "Código": moeda.get("code"),
            "Valor em R$": round(moeda.get("value", 0), 2),
            "Fonte": moeda.get("source")
        })

    # Criar o DataFrame
    df = pd.DataFrame(tabela)

    # Exibir a tabela
    st.markdown("### 📊 Tabela com Cotações das Moedas Estrangeiras")
    st.dataframe(df, use_container_width=True)

else:
    st.error("Erro ao acessar a API da BrasilAPI.")
           
