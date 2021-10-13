import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

tickers = pd.read_csv("data/ticker_list.csv")

symbols = ["BTC", "ETH", "D", "MSFT"]

st.title("Crypto tracker")
option = st.selectbox("Please select a ticker:", symbols)

start_date = st.date_input('Start date :')
end_date = st.date_input('Finish date:')

chosen_symbol = yf.Ticker(option)
df = chosen_symbol.history(start = start_date, end = end_date)

# def open_close_plot():
#     plt.figure(dpi=500)
#     fig = sns.lineplot(df['Open'], df['Close'])
#     return st.pyplot(fig = fig)

chart_data = df[['Open', 'Close']]

st.line_chart(chart_data)