import pandas as pd
from sklearn.linear_model import LogisticRegression

# Your data from yesterday
data = {
    "marks": [90, 75, 88, 40, 95, 55, 70, 30],
    "result": [1, 0, 1, 0, 1, 0, 0, 0]  # 1 = Pass, 0 = Fail
}
df = pd.DataFrame(data)

# Train the model
X = df[["marks"]]
y = df["result"]
model = LogisticRegression()
model.fit(X, y)

print("Model trained!")

# Now predict for new students
for marks in [85, 60, 95]:
    prediction = model.predict(pd.DataFrame([[marks]], columns=["marks"]))[0]
    print(f"Marks {marks} -> {'Pass' if prediction == 1 else 'Fail'}")