import pandas as pd

def load_data(path="data/concrete_cleaned.csv"):
    df = pd.read_csv(path)
    df.columns = df.columns.str.strip()  # Ensure no extra spaces
    X = df.drop(columns=["strength"])
    y = df["strength"]
    return X, y
