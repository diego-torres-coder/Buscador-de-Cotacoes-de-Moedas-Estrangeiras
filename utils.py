import requests


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


def obter_cotacoes():
    pass
