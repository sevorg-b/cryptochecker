import yfinance as yf
import pandas as pd
import datetime
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

current_date = datetime.datetime.today().strftime("%m-%d-%Y")

tickers = pd.read_csv("data/ticker_list.csv")

msft = yf.Ticker("MSFT")

symbols = ["MSFT", "ETH", "BTC", "D"]

st.markdown("<h1 style='text-align: center;'>Crypto tracker</h1>", unsafe_allow_html=True)
st.text("\n")

option = st.selectbox("Please select a currency to investigate:", symbols)
chosen_symbol = yf.Ticker(option)

start_date = st.date_input('Please chose a start date :', datetime.date(2019, 1, 1))
end_date = st.date_input('Please choose a finish date:', datetime.date(2021, 1, 1))

df = chosen_symbol.history(start = start_date, end = end_date)

st.markdown("<h1 style='text-align: center;'>Historic currency performance</h1>", unsafe_allow_html=True)
fig = go.Figure(data=[go.Candlestick(x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'])])
fig.update_layout(
    width=800,
    height=800,)

st.plotly_chart(fig)

### add in buying/selling reccomendations
reccomendations = pd.DataFrame(chosen_symbol.recommendations)

### Top reccomender
st.markdown("<h1 style='text-align: center; '>Business insights</h1>", unsafe_allow_html=True)
st.write(
    "What actions are firms reccomending?"
)
def countplot():
    plt.figure(figsize = (5, 5), dpi = 250)
    fig = reccomendations['To Grade'].value_counts().plot(kind="barh")
    st.pyplot(fig.figure)

if len(reccomendations) > 1:
    countplot()
else:
    st.write("Sorry, no reccomendations were found for this currency!")

### add in sustanability report








