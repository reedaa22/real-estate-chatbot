import pandas as pd

def load_data():

    df = pd.read_csv("data/Houses.csv")

    df.columns = df.columns.str.strip()

    numeric_columns = ["Price", "Bedrooms", "Bathrooms", "Area"]

    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna(subset=["Price", "City"])

    return df

def search_properties(df, filters):

    results = df.copy()

    if "city" in filters and filters["city"]:
        results = results[
            results["City"].str.contains(filters["city"], case=False, na=False)
        ]

    if "bedrooms" in filters and filters["bedrooms"]:
        results = results[
            results["Bedrooms"] == filters["bedrooms"]
        ]

    if "max_price" in filters and filters["max_price"]:
        results = results[
            results["Price"] <= filters["max_price"]
        ]

    return results.head(10)