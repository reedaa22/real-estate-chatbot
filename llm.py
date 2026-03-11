from groq import Groq
import json
import os

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


def extract_filters(user_query):

    prompt = f"""
You are a real estate assistant.

Extract property search filters from the user's request.

Return ONLY valid JSON.

Allowed fields:
- city
- bedrooms
- max_price

If a field is missing return null.

User request:
{user_query}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    content = response.choices[0].message.content.strip()

    try:
        return json.loads(content)

    except json.JSONDecodeError:

        start = content.find("{")
        end = content.rfind("}")

        if start != -1 and end != -1:
            json_text = content[start:end+1]
            return json.loads(json_text)

        return{}


def generate_response(user_query, results_text):

    prompt = f"""
You are a professional real estate assistant.

User request:
{user_query}

Search results:
{results_text}

IMPORTANT:
Reply in the SAME language as the user.

Rules:
- If the user writes Arabic reply in Arabic
- If the user writes English reply in English
- Be friendly
- Suggest good options
- Ask one follow-up question
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content.strip()