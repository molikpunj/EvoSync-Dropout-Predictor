import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

data = {
    "years_in_degree": [1, 2, 3, 4, 2, 1, 3, 4],
    "cgpa": [7.8, 6.5, 5.2, 8.0, 4.5, 9.0, 6.0, 7.0],
    "attendance": [85, 60, 40, 90, 30, 95, 55, 70],
    "fee_defaults": [0, 1, 1, 0, 1, 0, 1, 0],
    "leave_apps": [2, 5, 6, 1, 7, 0, 4, 3],
    "dropout": [0, 1, 1, 0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)

X = df.drop("dropout", axis=1)
y = df["dropout"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

with open("dropout_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved as dropout_model.pkl")
