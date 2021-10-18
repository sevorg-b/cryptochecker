import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import yfinance as yf
import time
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error
from sklearn.linear_model import LinearRegression
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

df = yf.download('BTC-USD', '2015-01-01', '2021-10-01')

X = df[['Open', 'High', 'Low', 'Volume']]
y = df['Adj Close'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 101)
scaler = MinMaxScaler()
X_train, X_test = scaler.fit_transform(X_train), scaler.fit_transform(X_test)


# noinspection PyGlobalUndefined
# class model_development():
#                         # (4, 1, 'relu', 'adam', 'mse', 250, 1)
#     def __init__ (self, layers, output_layer, activation_function, optimizer_function, loss_function, n_epochs, verbose):
#         self.layers = layers
#         self.output_layer = output_layer
#         self.activation_function = activation_function
#         self.optimizer_function = optimizer_function
#         self.loss_function = loss_function
#         self.n_epochs = n_epochs
#         self.verbose = verbose

def train_network(layers, output_layer, activation_function, optimizer_function, loss_function, n_epochs):
    model = keras.Sequential(
        [
            Dense(layers, activation = activation_function),
            Dense(layers, activation = activation_function),
            Dense(layers, activation = activation_function),
            Dense(output_layer),
        ])

    model.compile(optimizer = optimizer_function, loss = loss_function)
    model.fit(x = X_train, y = y_train, validation_data = (X_test, y_test), batch_size = 64, epochs = n_epochs, verbose = 1)

    loss_df = pd.DataFrame(model.history.history)
    loss_df.plot()

    test_prediction = model.predict(X_test)
    test_prediction = pd.Series(test_prediction.reshape(739,))

    pred_df = pd.DataFrame({
        'actual': y_test,
        'predicted': test_prediction
    })

    sns.scatterplot(x='actual', y = 'predicted', data = pred_df)
    plt.show()

train_network(4, 1, 'relu', 'adam', 'mse', 400)
