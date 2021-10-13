import yfinance as yf
import matplotlib.pyplot as plt
import streamlit as st

btc = yf.Ticker("BTC-USD")
df = btc.history(start = "2020-01-01", end = "2020-06-01")

print(df.columns)


def open_close_plot (data):
    plt.plot(data['Open'], "g", linestyle = "-", linewidth = 1.5)
    plt.plot(data['Close'], "r", linestyle = "-", linewidth = 1.5)
    plt.legend(['Open', 'Close'])
    return plt.show()


open_close_plot(df)
