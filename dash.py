import pandas as pd
import pandas_datareader as data
import streamlit as st
import numpy as np
import yfinance as yf
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
from app import modeldev

st.markdown("<h1 style='text-align: center;'>Crypto analysis</h1>", unsafe_allow_html=True)
st.text(" ")
st.text(" ")

currency_choice = st.radio("Please choose your desired currency:", ("USD", "GBP", "CAD"))

gbp = ["MSFT", "BTC-GBP", "ETH-GBP", "BNB-GBP", "DOGE-GBP"]
usd = ["MSFT", "BTC-USD", "ETH-USD", "BNB-USD", "DOGE-USD"]
cad = ["MSFT", "BTC-CAD", "ETH-CAD", "BNB-CAD", "DOGE-CAD"]

if currency_choice == 'USD':
    choice = st.selectbox("Select a stock to view:", usd)
    get_ticker = yf.Ticker(choice)
    print(choice)
elif currency_choice == 'GBP':
    choice = st.selectbox("Select a stock to view:", gbp)
    get_ticker = yf.Ticker(choice)
else:
    choice = st.selectbox("Select a stock to view:", cad)
    get_ticker = yf.Ticker(choice)

start_date = st.date_input('Please chose a start date :', dt.date(2015, 1, 1))
end_date = st.date_input('Please choose a finish date:', dt.date(2021, 10, 1))

df = get_ticker.history(start = start_date, end = end_date)

### Candlestick plot

st.subheader("{} performance between {} and {}".format(choice, start_date, end_date))
def candlestick():
    fig = go.Figure(data=[go.Candlestick(x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'])])
    fig.update_layout(width=800, height=800,)
    return st.plotly_chart(fig)

candlestick()
### View as tabular data
tab_choice = ["Yes", "No"]
tab_choice = st.radio("Would you like to view performance in tabular format?", tab_choice)
tab = st.radio

### Company background
comp_background = get_ticker.info

description = 'description'
business_summary = "longBusinessSummary"

st.subheader("{} description".format(choice))
if description in comp_background:
    st.write(comp_background['description'])
else:
    st.write(comp_background['longBusinessSummary'])

### Sell/Buy reccomendations
st.markdown("<h1 style='text-align: center;'>Reccomendations</h1>", unsafe_allow_html=True)
st.text("")
st.write(
    "Here are the reccomendations for {}:".format(str(choice))
)

def countplot(data):
    plt.figure(figsize = (5, 5), dpi = 500)
    plt.title("Agg reccomendation options")
    plt.ylabel("Reccomendation")
    plt.xlabel("Count")
    fig = data['To Grade'].value_counts().plot(kind="barh")

    st.pyplot(fig.figure)

decision = ['All', 'Single firm']

single_many_firms = st.radio("Would you like to see an aggregate of firm reccomendations or see a single firm's reccomendation?", decision)

reccomendations = get_ticker.recommendations

if reccomendations is None:
    st.write("Sorry! There are no recommendations for {}".format(str(choice)))
elif single_many_firms == "All":
    countplot(reccomendations)
else:
    firm = reccomendations['Firm'].unique()
    firm = np.sort(firm)
    selection = st.selectbox("Chose a firm to see their recommendations:", firm)
    recc_df = reccomendations[['Firm', 'To Grade']]
    recc_df = recc_df[recc_df['Firm'] == selection]
    countplot(recc_df)

st.write(modeldev())








