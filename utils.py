from datetime import datetime as dt
from datetime import date
from datetime import timedelta
import pandas as pd
import requests


def formatar_data(data):
    # Converte a string numa data no formato mm/dd/aaaa
    data_formatada = dt.strptime(data, '%m-%d-%Y')

    # Retorna a data formatada como uma string
    return data_formatada.strftime('%d/%m/%Y')


def formatar_data_api(data):
    # Converte a data numa string com a seguinte formatação: mm/dd/aaaa
    return data.strftime('%m-%d-%Y')


def obter_maior_data():
    '''Retorna a data do dia anterior'''
    return date.today() - timedelta(days=1)


def obter_moedas():
    # Endpoint da API para obter as moedas disponíveis
    url = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/Moedas?$top=100&$format=json&$select=simbolo'

    # Dados da resposta da requisição GET
    dados_resposta = requests.get(url).json()

    # Lista auxiliar para armazenar as moedas disponíveis
    moedas_disponiveis = []

    for valor in dados_resposta['value']:
        moedas_disponiveis.append(valor['simbolo'])

    return moedas_disponiveis


def obter_cotacao(moeda, data):
    # Endpoint da API para obter a cotação da moeda selecionada na data especificada
    url = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoMoedaDia(moeda=@moeda,dataCotacao=@dataCotacao)?@moeda='{moeda}'&@dataCotacao='{data}'&$top=1&$orderby=dataHoraCotacao%20desc&$format=json&$select=cotacaoVenda"

    # Dados da resposta da requisição
    dados_resposta = requests.get(url).json()

    # Retorna a cotação de venda da moeda
    return dados_resposta['value'][0]['cotacaoVenda']


def obter_cotacoes(moedas, data_inicial, data_final):
    cotacoes = []

    # Percorre a lista de moedas
    for moeda in moedas:
        # Endpoint da API para obter a cotação de uma moeda num período especificado
        url = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoMoedaPeriodo(moeda=@moeda,dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@moeda='{moeda}'&@dataInicial='{data_inicial}'&@dataFinalCotacao='{data_final}'&$top=10000&$filter=tipoBoletim%20eq%20'Fechamento'&$orderby=dataHoraCotacao%20desc&$format=json&$select=cotacaoVenda,dataHoraCotacao,tipoBoletim"
        
        # Dados da resposta da requisição
        dados_resposta = requests.get(url).json()

        for valor in dados_resposta['value']:
            # Cotação de venda da moeda
            cotacao = valor['cotacaoVenda']

            # Data da cotação
            data_cotacao = valor['dataHoraCotacao']

            # Converte a string num objeto de data
            data_cotacao = dt.strptime(data_cotacao, '%Y-%m-%d %H:%M:%S.%f')

            # Converte o objeto de data numa string
            data_cotacao = data_cotacao.strftime('%d/%m/%Y')

            # Acrescenta um item a lista
            cotacoes.append((moeda, data_cotacao, cotacao))

    return cotacoes

