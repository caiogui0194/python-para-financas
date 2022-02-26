import MetaTrader5 as mt5
import time
import pandas as pd

ativo1 = 'WLMM4F'
ativo2 = 'ITUB4'

mt5.initialize()

selecionado1 = mt5.symbol_select(ativo1)
selecionado2 = mt5.symbol_select(ativo2)

while True:
    itens = mt5.market_book_get(ativo1)
    for item in itens:
        # print(pd.DataFrame.from_dict(item._asdict(), orient = 'index').reset_index())
        df = pd.DataFrame(item._asdict(), index = [item,])

    time.sleep(5)