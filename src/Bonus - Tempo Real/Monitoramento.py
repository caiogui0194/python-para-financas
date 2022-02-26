import MetaTrader5 as mt5
import time
import pandas as pd

pd.set_option('display.max_columns', 500) # número de colunas mostradas
pd.set_option('display.width', 1500)      # max. largura máxima da tabela exibida

mt5.initialize()


while True:

    positions = mt5.positions_get()

    if positions == None:
        print("Sem posições abertas")
    elif len(positions) > 0:
        df = pd.DataFrame(list(positions), columns= positions[0]._asdict().keys())
        df['time'] = pd.to_datetime(df['time'], unit='s')
        df.drop(['time_update', 'time_msc', 'time_update_msc', 'external_id'], axis=1, inplace=True)
        print(df)


    time.sleep(5)


