import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Membaca dataset
df = pd.read_csv("Regresis Penjualan Minuman.csv")
print("Data Awal:")
print(df.head())


X = df[['x']]  
y = df['y']    


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)

# 6. Menghitung performa model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Koefisien (Slope): {model.coef_[0]:.2f}")
print(f"Intercept: {model.intercept_:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R² Score: {r2:.2f}")

# 7. Visualisasi hasil prediksi
plt.scatter(X, y, color='blue', label='Data Asli')
plt.plot(X, model.predict(X), color='red', linewidth=2, label='Garis Regresi')
plt.title("Hubungan Suhu dan Penjualan Minuman")
plt.xlabel("x (Hari / Suhu Harian)")
plt.ylabel("y (Penjualan Minuman)")
plt.legend()
plt.grid(True)
plt.show()
