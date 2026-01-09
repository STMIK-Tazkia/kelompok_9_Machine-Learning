import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input

np.random.seed(42)

temperature = np.random.randint(20, 35, size=60)
sales = temperature * 3 + np.random.randint(-10, 10, size=60)

data = pd.DataFrame({
    "Temperature": temperature,
    "Sales": sales
})

plt.figure()
plt.scatter(data["Temperature"], data["Sales"])
plt.xlabel("Suhu Harian (°C)")
plt.ylabel("Jumlah Penjualan")
plt.title("Hubungan Suhu Harian dan Penjualan Minuman")
plt.show()

X = data[["Temperature"]].values
y = data["Sales"].values

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

y_pred_lr = lr_model.predict(X_test)
mse_lr = mean_squared_error(y_test, y_pred_lr)

dl_model = Sequential([
    Input(shape=(1,)),
    Dense(16, activation="relu"),
    Dense(8, activation="relu"),
    Dense(1)
])

dl_model.compile(optimizer="adam", loss="mse")

dl_model.fit(
    X_train,
    y_train,
    epochs=100,
    batch_size=8,
    validation_split=0.2,
    verbose=0
)

y_pred_dl = dl_model.predict(X_test)
mse_dl = mean_squared_error(y_test, y_pred_dl)

comparison = pd.DataFrame({
    "Model": ["Linear Regression", "Deep Learning"],
    "MSE": [mse_lr, mse_dl]
})

print(comparison)

plt.figure()
plt.scatter(X_test, y_test, label="Data Aktual")
plt.scatter(X_test, y_pred_dl, label="Prediksi Deep Learning")
plt.xlabel("Suhu (Scaled)")
plt.ylabel("Penjualan")
plt.title("Data Aktual vs Prediksi Deep Learning")
plt.legend()
plt.show()
