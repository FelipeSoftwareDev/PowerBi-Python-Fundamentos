# shift + enter abre uma janela interativa do jupyter, facilita a visualização das saídas
# sem ter que executar o código toda hora

import yfinance as yf

def carregar_dados(ticker):
    df = yf.Ticker(ticker).history("1y")
    df.reset_index(inplace=True)
    df['ticker'] = ticker.split(".")[0]
    return df

petrobras = carregar_dados("PETR4.SA")
bb = carregar_dados("BBAS3.SA")
vale = carregar_dados("VALE3.SA")

#Para ver as informações carregadas
petrobras.head()

#Para ver os datatypes
petrobras.info()

vale.info()

bb.head()