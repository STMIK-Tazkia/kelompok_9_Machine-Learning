import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv("ai4i2020.csv")
data = data.drop(columns=['UDI', 'Product ID'])
data = pd.get_dummies(data, columns=['Type'], drop_first=True)

X = data.drop(columns=['Machine failure'])
y = data['Machine failure']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)

print(f"Akurasi Model Random Forest: {acc:.2f}")