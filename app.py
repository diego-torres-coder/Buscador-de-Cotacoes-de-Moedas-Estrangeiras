# Importa a biblioteca streamlit com o apelido st
import streamlit as st

# Importa o pandas com o apelido pd
import pandas as pd

# Importa o módulo requests
import requests

# Importa o submódulo datetime do módulo datetime
from datetime import datetime as dt

# Importa o submódulo date do módulo datetime
from datetime import date

# Importa o submódulo timedelta do módulo datetime
from datetime import timedelta

# Importação de funções auxiliares de um script próprio
from utils import (
    obter_moedas, 
    obter_cotacao, 
    obter_cotacoes, 
    formatar_data, 
    formatar_data_api,
    obter_maior_data
)


# Define o título da aplicação
st.title('Cotações de Moedas')

# Título da seção para cotação de uma única moeda
st.header('Cotação de uma Moeda')

# Escreve uma instrução para o usuário
st.write('Obtenha a cotação para a moeda selecionada na data especificada.')

# Obtém a lista de moedas disponíveis na API do Banco Central do Brasil
moedas_disponiveis = obter_moedas()

# Cria duas colunas
col1, col2 = st.columns(2)

# Criação de conteúdo para a primeira coluna
with col1:
    # Cria um menu suspenso com as moedas disponíveis
    moeda = st.selectbox('Selecione uma moeda:', options=moedas_disponiveis)

# Criação de conteúdo para a segunda coluna
with col2:
    # Obtém a data selecionada pelo usuário
    data_selecionada = st.date_input('Escolha uma data:', value=obter_maior_data(), max_value=obter_maior_data())

    # Obtém a data no formato exigido pela API
    data_formatada_api = formatar_data_api(data_selecionada)

    # Data para ser exibida
    data = formatar_data(data_formatada_api)

# Verifica se o usuário preencheu todos os campos corretamente
if moeda and data_selecionada:
    # Verifica se o usuário clicou no botão
    if st.button('Obter Cotação'):
        # Obtém a cotação para a moeda na data selecionada
        cotacao = obter_cotacao(moeda, data_formatada_api)

        # Exibe uma mensagem com a cotação da moeda escolhida na data especificada
        st.write(f'A cotação da moeda {moeda} no dia {data} era de R${cotacao:.2f}')
else:
    st.error('Preencha todos os campos corretamente.')

# Cabeçalho da seção para obter a cotação de diversas moedas
st.header('Cotação para Diversas Moedas')

# Instrução para o usuário
st.write('Obtenha a cotação para diversas moedas carregando um CSV com as moedas na primeira coluna.')

# Armazena o arquivo que o usuário carregou
arquivo = st.file_uploader('Selecione um arquivo CSV:', type='csv')

# Cria duas colunas
col1, col2 = st.columns(2)

# Criação do conteúdo da primeira coluna
with col1:
    # Data inicial
    data_inicial = st.date_input('Selecione a data inicial:', value=obter_maior_data(), max_value=obter_maior_data())

    # Data inicial no formato da API
    data_inicial_api = formatar_data_api(data_inicial)

with col2:
    # Data final
    data_final = st.date_input('Selecione a data final:', value=obter_maior_data(), max_value=obter_maior_data())

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