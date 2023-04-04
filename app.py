# Importações de bibliotecas
import streamlit as st
import pandas as pd
import requests
from datetime import datetime as dt
from datetime import date
from datetime import timedelta

# Importação de funções auxiliares de um script próprio
from utils import (
    obter_moedas, 
    obter_cotacao, 
    obter_cotacoes, 
    formatar_data, 
    formatar_data_api
)


st.title('Cotações de Moedas')

st.header('Cotação de uma Moeda')

st.write('Obtenha a cotação para a moeda selecionada na data especificada.')

# Obtém a lista de moedas disponíveis na API do Banco Central do Brasil
moedas_disponiveis = obter_moedas()

col1, col2 = st.columns(2)

with col1:
    moeda = st.selectbox('Selecione uma moeda:', options=moedas_disponiveis)


with col2:
    maior_data = date.today() - timedelta(days=1)

    # Obtém a data selecionada pelo usuário
    data = st.date_input('Escolha uma data:', value=maior_data, max_value=maior_data)

    # Obtém a data no formato exigido pela API
    data_formatada_api = formatar_data_api(data)

    # Data para ser exibida
    data_selecionada = formatar_data(data_formatada_api)

# Verifica se o usuário clicou no botão
if st.button('Obter Cotação'):
    # Obtém a cotação para a moeda na data selecionada
    cotacao = obter_cotacao(moeda, data_formatada_api)

    st.write(f'A cotação da moeda {moeda} no dia {data_selecionada} era de R${cotacao:.2f}')

st.header('Cotação para Diversas Moedas')

st.write('Obtenha a cotação para diversas moedas carregando um CSV com as moedas na primeira coluna.')

arquivo = st.file_uploader('Selecione um arquivo CSV:', type='csv')

col1, col2 = st.columns(2)

with col1:
    # Data inicial
    data_inicial = st.date_input('Selecione a data inicial:')

    # Data inicial no formato da API
    data_inicial_api = formatar_data_api(data_inicial)

with col2:
    # Data final
    data_final = st.date_input('Selecione a data final:')

    # Data final no formato da API
    data_final_api = formatar_data_api(data_final)

if st.button('Obter Cotações'):
    if arquivo:
        try:
            # Lê o arquivo CSV
            df_moedas = pd.read_csv(arquivo)

            # Obtém uma lista com as moedas da primeira coluna
            moedas = list(df_moedas['Moedas'])

            # Obtém as cotações das moedas especificadas no intervalo de datas solicitado
            cotacoes = obter_cotacoes(moedas, data_inicial_api, data_final_api)

            # Cria um dataframe com as cotações das moedas
            df_cotacoes = pd.DataFrame(
                data=cotacoes,
                columns=['Moeda', 'Data', 'Cotação (R$)']
            )

            st.write(df_cotacoes)

            # Obtém um CSV a partir do df
            csv = df_cotacoes.to_csv().encode('utf-8')

            st.download_button(
                label='Baixar CSV',
                data=csv,
                file_name='cotacoes.csv',
                mime='text/csv'
            )

        except:
            st.error('Ocorreu um erro durante o processamento dos dados.')
    else:
        st.write('Nenhum arquivo foi carreagado.')