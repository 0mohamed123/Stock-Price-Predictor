import yfinance as yf
import pandas as pd

stock_symbol = "TSLA"
data = yf.download(stock_symbol, start="2020-01-01", end="2025-01-01")

data.to_csv("stock_data.csv")

print("stock_data.csv downloaded successfully")