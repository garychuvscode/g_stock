# for stock analysis, test for yfinance

import yfinance as yf
import pandas as pd
import xlwings as xw
import numpy as np
# atof using import
import locale as lo

df = yf.Ticker("2330.TW").history(period="20d")
print(df)
