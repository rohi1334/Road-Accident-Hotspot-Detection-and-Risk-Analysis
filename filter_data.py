import pandas as pd

df = pd.read_csv("data/raw/AccidentsBig.csv")

df.columns = df.columns.str.lower()

df = df[["latitude", "longitude"]]

df = df.dropna()

# Filter AP + TS

df = df[
    (df["latitude"] > 13) &
    (df["latitude"] < 20.5) &
    (df["longitude"] > 77) &
    (df["longitude"] < 85.5)
]

# add empty city column

df["city"] = ""

df.to_csv("data/raw/Accidents_AP_TS.csv", index=False)

print("Saved filtered file")