import pandas as pd

def load_data():

    df = pd.read_csv("data/Houses.csv")

    df.columns = df.columns.str.strip()

    numeric_columns = ["Price", "Bedrooms", "Bathrooms", "Area"]

    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna(subset=["Price", "City"])

    return df