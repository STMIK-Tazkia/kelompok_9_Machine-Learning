# 1. Import library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


# 2. Load dataset
# Dataset berisi kolom: Bulan, Minuman, x, y
# Kolom x direpresentasikan sebagai suhu harian (Temperature)
data = pd.read_csv("Regresis Penjualan Minuman.csv")

# 3. Menentukan variabel input (Temperature) dan output (Sales)
X = data[['x']].values          # Suhu Harian (Temperature)
y = data[['Minuman']].values   # Jumlah Penjualan Minuman (Sales)

# 4. Normalisasi data
# Digunakan agar proses training Deep Learning lebih stabil
scaler_X = MinMaxScaler()
scaler_y = MinMaxScaler()

X = scaler_X.fit_transform(X)
y = scaler_y.fit_transform(y)

# 5. Pembagian data training dan testing
# 80% data training, 20% data testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 6. Perancangan arsitektur Deep Learning (Neural Network)
# Multilayer Perceptron dengan 2 hidden layer
model = Sequential()
model.add(Dense(16, activation='relu', input_shape=(1,)))
model.add(Dense(8, activation='relu'))
model.add(Dense(1))

# 7. Kompilasi model
model.compile(
    optimizer='adam',
    loss='mse'
)

# 8. Pelatihan model Deep Learning
history = model.fit(
    X_train,
    y_train,
    epochs=100,
    batch_size=4,
    validation_split=0.1,
    verbose=1
)

# 9. Evaluasi model Deep Learning
y_pred_dl = model.predict(X_test)
mse_dl = mean_squared_error(y_test, y_pred_dl)

print("MSE Deep Learning:", mse_dl)

# 10. Perbandingan dengan metode Machine Learning tradisional
from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(X_train, y_train)

y_pred_lr = lr.predict(X_test)
mse_lr = mean_squared_error(y_test, y_pred_lr)

print("MSE Linear Regression:", mse_lr)

# 11. Visualisasi hasil prediksi
plt.scatter(X_test, y_test, label="Data Aktual")
plt.scatter(X_test, y_pred_dl, color='red', label="Prediksi Deep Learning")
plt.xlabel("Suhu Harian (Temperature)")
plt.ylabel("Jumlah Penjualan Minuman")
plt.legend()
plt.show()
