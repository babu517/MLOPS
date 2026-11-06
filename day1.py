import pandas as pd

data = {
    "name": ["Asha", "Ravi", "Meena"],
    "marks": [90, 75, 88]
}

df = pd.DataFrame(data)
df["result"] = ["Pass" if m >= 80 else "Fail" for m in df["marks"]]
print(df)

df.to_csv("results.csv", index=False)
print("Saved!")