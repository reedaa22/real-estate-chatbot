import sys
sys.stdout.reconfigure(encoding='utf-8')
from utils import load_data, search_properties
from llm import extract_filters, generate_response

df = load_data()

# جرب عربي أو إنجليزي
user_query = "عايز شقة 3 غرف في مدينة نصر تحت 3000000"
# user_query = "I want a 3 bedroom apartment in Nasr City under 3000000"

filters = extract_filters(user_query)

results = search_properties(df, filters)

if results.empty:

    print("Extracted Filters:")
    print(filters)

    print("\nChatbot Reply:")
    print("لم أجد نتائج مطابقة تمامًا. هل تحب أوسع نطاق البحث أو أغير المدينة؟")

else:

    columns = ["Type","Price","Bedrooms","Bathrooms","Area","City"]

    available_columns = [c for c in columns if c in results.columns]

    results_text = results[available_columns].to_string(index=False)

    reply = generate_response(user_query, results_text)

    print("Extracted Filters:")
    print(filters)

    print("\nSearch Results:")
    print(results_text)

    print("\nChatbot Reply:")
    print(reply)