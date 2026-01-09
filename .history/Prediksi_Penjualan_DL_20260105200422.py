import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

data = pd.read_csv("Regresis Penjualan Minuman.csv")

X = data[['x']].values          
y = data[['Minuman']].values   

scaler_X = MinMaxScaler()
scaler_y = MinMaxScaler()

X = scaler_X.fit_transform(X)
y = scaler_y.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = Sequential()
model.add(Dense(16, activation='relu', input_shape=(1,)))
model.add(Dense(8, activation='relu'))
model.add(Dense(1))

model.compile(
    optimizer='adam',
    loss='mse'
)

history = model.fit(
    X_train,
    y_train,
    epochs=100,
    batch_size=4,
    validation_split=0.1,
    verbose=1
)

y_pred_dl = model.predict(X_test)
mse_dl = mean_squared_error(y_test, y_pred_dl)

print("MSE Deep Learning:", mse_dl)

from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(X_train, y_train)

y_pred_lr = lr.predict(X_test)
mse_lr = mean_squared_error(y_test, y_pred_lr)

print("MSE Linear Regression:", mse_lr)

plt.scatter(X_test, y_test, label="Data Aktual")
plt.scatter(X_test, y_pred_dl, color='red', label="Prediksi Deep Learning")
plt.xlabel("Suhu Harian (Temperature)")
plt.ylabel("Jumlah Penjualan Minuman")
plt.legend()
plt.show()
