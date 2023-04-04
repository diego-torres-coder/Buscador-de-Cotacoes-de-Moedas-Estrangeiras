# Importações de bibliotecas
import streamlit as st
import pandas as pd
import requests
from datetime import datetime as dt

# Importação de funções auxiliares de um script próprio
from utils import obter_moedas, obter_cotacao, obter_cotacoes


st.title('Cotações de Moedas')

st.header('Cotação de uma Moeda')

st.write('Obtenha a cotação para a moeda selecionada na data especificada.')

# Obtém a lista de moedas disponíveis na API do Banco Central do Brasil
moedas_disponiveis = obter_moedas()

col1, col2 = st.columns(2)

with col1:
    moeda = st.selectbox('Selecione uma moeda:', options=moedas_disponiveis)


with col2:
    # Obtém a data selecionada pelo usuário
    data = st.date_input('Escolha uma data:')

    # Formata a data
    data = data.strftime('%m/%d/%Y')

    data_formatada = dt.strptime(data, '%m/%d/%Y')
    data_selecionada = data_formatada.strftime('%d/%m/%Y')

    # Obtém a cotação para a moeda na data selecionada
    cotacao = obter_cotacao(moeda, data)

if st.button('Obter Cotação'):
    st.write(f'A cotação da moeda {moeda} no dia {data_selecionada} era de R${cotacao:.2f}')

st.header('Cotação para Diversas Moedas')

st.write('Obtenha a cotação para diversas moedas carregando um CSV com as moedas na primeira coluna.')

arquivo = st.file_uploader('Selecione um arquivo CSV:', type='csv')

col1, col2 = st.columns(2)

with col1:
    data_inicial = st.date_input('Selecione a data inicial:')

with col2:
    data_final = st.date_input('Selecione a data final:')

st.button('Obter Cotações')