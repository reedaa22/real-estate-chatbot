import streamlit as st

from utils import load_data, search_properties
from llm import extract_filters, generate_response

st.title("🏠 Real Estate AI Chatbot")

df = load_data()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("Ask about properties...")

if user_input:

    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.write(user_input)

    filters = extract_filters(user_input)

    results = search_properties(df, filters)

    if results.empty:
        reply = "لم أجد نتائج مطابقة، هل تريد تغيير المدينة أو الميزانية؟"
    else:
        columns = ["Type","Price","Bedrooms","Bathrooms","Area","City"]

        available_columns = [c for c in columns if c in results.columns]

        results_text = results[available_columns].to_string(index=False)

        reply = generate_response(user_input, results_text)

    with st.chat_message("assistant"):
        st.write(reply)

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )