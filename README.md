# Buscador de Cotações de Moedas Estrangeiras

Este projeto usa o **Streamlit** — um frameword do Python para construção de **data apps** — para criar uma aplicação para buscar cotações de moedas estrangeiras por meio de requisições GET para uma API do Banco Central do Brasil (BACEN). 

Com esta aplicação o usuário pode buscar a cotação de uma moeda em uma data específica, tal como mostrado na captura de tela a seguir:

![Captura de tela da aplicação para busca da cotação de uma moeda](/buscador-cotacao-unica.png "Obtendo a cotação de uma moeda em uma data")

Caso o usuário deseje obter as cotações de diversas moedas em um intervalo de datas, ele pode os símbolos das moedas para as quais ele deseja obter as cotações e definir o intervalo de datas nos campos de data inicial e final. Veja na captura de tela abaixo o resultado deste tipo de operação:

![Captura de tela da aplicação para busca das cotações de diversas moedas](/buscador-cotacao-multipla.png "Obtendo cotações de diversas moedas")

Note que o usuário também tem a possibilidade de baixar um arquivo CSV com as cotações das moedas para o intervalo de datas especificado.

## Como Reproduzir este Projeto

Inicialmente, navegue para a pasta em que deseja clonar este projeto. Em seguida, digite o seguinte comando no terminal:

```bash
git clone https://github.com/diego-torres-coder/Buscador-de-Cotacoes-de-Moedas-Estrangeiras.git
```

Navegue para a pasta que você baixou no passo anterior:

```bash
cd Buscador-de-Cotacoes-de-Moedas-Estrangeiras/
```

Crie um ambiente conda para o projeto:

```bash
conda create -n stenv-buscador-cotacoes-moedas python=3.10
```

Com o ambiente criado, você deve ativá-lo:

```bash
conda activate stenv-buscador-cotacoes-moedas
```

Com o ambiente ativo, instale as dependências do projeto:

```bash
pip install numpy openpyxl pandas requests streamlit
```

Alternativamente, você pode instalar as dependências deste projeto a partir do arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

Seu último passo consiste em executar o script `app.py` com o seguinte comando:

```bash
streamlit run app.py
```