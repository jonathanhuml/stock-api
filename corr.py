import yfinance as yf
import numpy as np
import seaborn
import matplotlib.pyplot as plt

start_date = '2019-11-01'
end_date = '2024-02-04'

tickers = 'AMKBY ASML GLD MATX NET NSC TSM AGG LLY'

# 'NET TSM NVDA ASML MATX UNP NSC AMKBY AGG LLY ITW IAU GLD AMZN META'

data = yf.download(tickers, start_date, end_date)
prices = data[["Adj Close"]]

print(prices)
print('-------------------------------')
print('PRICE VARIANCE')
print(prices.std())
print('-------------------------------')
cum_return_pct = ((prices.iloc[-1] - prices.iloc[0]) / prices.iloc[0] ) * 100
print('PERCENTAGE RETURN OVER TIME PERIOD')
print(cum_return_pct)
print('-------------------------------')
print(prices.corr())
# seaborn.heatmap(prices.corr(), cmap='cividis')
# plt.show()
