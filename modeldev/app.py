import tensorflow as tf
from tensorflow import keras
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import yfinance as yf

lookup_step = 1,
data = yf.download('AAPL', '1980-01-01', '2021-10-01')
print(data.shape)
print(data.columns)

X = data.drop('Adj Close', axis = 1)
y = data['Adj Close']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

lr = LinearRegression()

lr.fit(X_train, y_train)

y_pred = lr.predict(X_test)

print("mean absolute error:", mean_absolute_error(y_test, y_pred))
print("mean squared error is:", mean_squared_error(y_test, y_pred))
print("RMSE", np.sqrt(mean_squared_error(y_test, y_pred)))
