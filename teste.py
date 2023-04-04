import requests


url = "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoMoedaPeriodo(moeda=@moeda,dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@moeda='USD'&@dataInicial='03-01-2023'&@dataFinalCotacao='03-31-2023'&$top=1&$orderby=dataHoraCotacao%20desc&$format=json&$select=cotacaoVenda,dataHoraCotacao"

dados_resposta = requests.get(url).json()

print(type(dados_resposta['value'][0]['dataHoraCotacao']))