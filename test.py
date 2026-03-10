from utils import load_data, search_properties

df = load_data()

filters = {
    "city": "Nasr City",
    "bedrooms": 3,
    "max_price": 3000000
}

results = search_properties(df, filters)

print(results)