import csv
import cryptocompare as cc

tickers = cc.get_coin_list()
tickerlist = tickers.keys()

with open("ticker_list.csv", 'w+') as f:
    wr = csv.writer(f)
    wr.writerow(tickerlist)