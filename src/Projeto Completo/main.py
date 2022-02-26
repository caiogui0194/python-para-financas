import MetaTrader5 as mt5
import pandas as pd

mt5.initialize()

ativos = []
setores = []
descricoes = []


symbols_information = mt5.symbols_get()