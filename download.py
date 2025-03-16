import yfinance as yf
import pandas as pd

# 选定股票和市场指数
stock_tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "NVDA", "JPM", "V", "PG", "DIS"]
market_ticker = "^GSPC"

# 下载数据
start_date = "2019-01-01"
end_date = "2024-01-01"
data = yf.download(stock_tickers + [market_ticker], start=start_date, end=end_date)

# 处理 MultiIndex，提取收盘价
adj_close_data = data["Close"]
print(adj_close_data.head())  # 确保数据结构正确

# 计算每日收益率
returns = adj_close_data.pct_change().dropna()
print(returns.head())  # 确保计算正确
