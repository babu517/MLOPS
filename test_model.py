import joblib

model = joblib.load("model.pkl")
print(model.predict([[55]]))
print(model.predict([[85]]))