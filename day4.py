import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

print("Day 4 started")

data = {"marks": [30, 40, 50, 60, 70, 80, 90], "pass": [0, 0, 0, 1, 1, 1, 1]}
df = pd.DataFrame(data)
X = df[["marks"]]
y = df["pass"]

print(df)
model = LogisticRegression()
model.fit(X, y)
joblib.dump(model, "model.pkl")
print("Model saved as model.pkl")