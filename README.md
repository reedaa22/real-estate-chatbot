# Real Estate AI Chatbot

## Project Overview

This project aims to build an **AI-powered real estate chatbot** that allows users to search for properties using natural language instead of traditional filters.

Instead of manually selecting filters such as city, price, and number of bedrooms, the user can type a request like:

"Show me a 3 bedroom apartment in Nasr City under 3 million."

The system will then:

1. Understand the user's request using an LLM (Large Language Model)
2. Convert the request into structured search filters
3. Search the property dataset
4. Return the most relevant results
5. Later connect the chatbot to a **website through an API**

This approach is known as:

**LLM + Structured Data Retrieval**

or

**Natural Language Property Search**

---

## Project Roadmap

The project will be developed through the following stages:

1. Project Setup  
2. Data Preparation  
3. Property Search Engine  
4. Conversational AI Layer (LLM)  
5. Chat Interface  
6. Backend API  
7. Website Integration  
8. System Improvements & Optimization  

Currently we have completed **Stage 1, Stage 2, and Stage 3**.

---

# 1. Stage 1 — Project Setup

## 1.1 Goal

Prepare the development environment and create the base structure of the project.

---

## 1.2 Create GitHub Repository

A GitHub repository was created to manage the project and enable collaboration.

Repository name:

```
real-estate-chatbot
```

This allows version control and team collaboration.

---

## 1.3 Clone Repository Locally

The repository was cloned to the local machine using:

```bash
git clone <repository_url>
```

This command downloads the project from GitHub to the local computer.

---

## 1.4 Open Project in VS Code

The project folder was opened in **Visual Studio Code** to start development.

---

## 1.5 Create Initial Project Structure

The following project structure was created:

```
real-estate-chatbot
│
├── data
│   └── Houses.csv
│
├── utils.py
├── test.py
├── README.md
```

Explanation:

**data/**  
Contains the dataset used in the project.

**utils.py**  
Contains helper functions used across the project.

**test.py**  
Used for testing project functionality.

**README.md**  
Contains documentation for the project.

---

# 2. Stage 2 — Data Preparation

## 2.1 Goal

Prepare and clean the dataset so that it can be used efficiently for property search.

---

## 2.2 Add Dataset

The real estate dataset was added to the project inside:

```
data/Houses.csv
```

The dataset contains property listings including:

- Property Type
- Price
- Bedrooms
- Bathrooms
- Area
- Furnished
- Level
- Compound
- Payment Option
- Delivery Date
- Delivery Term
- City

---

## 2.3 Create Data Loading Function

A function called `load_data()` was implemented in:

```
utils.py
```

This function loads and prepares the dataset.

---

## 2.4 Import Pandas

```python
import pandas as pd
```

Pandas is used to work with tabular datasets such as CSV files.

---

## 2.5 Read Dataset

```python
df = pd.read_csv("data/Houses.csv")
```

This reads the dataset and converts it into a **Pandas DataFrame**.

---

## 2.6 Clean Column Names

```python
df.columns = df.columns.str.strip()
```

This removes extra spaces from column names to avoid future errors.

---

## 2.7 Convert Numeric Columns

The following columns were converted to numeric format:

- Price
- Bedrooms
- Bathrooms
- Area

Example logic used:

```python
pd.to_numeric(...)
```

Invalid values are converted to `NaN`.

---

## 2.8 Remove Invalid Rows

Rows missing critical information such as **Price** or **City** were removed.

Example:

```python
df.dropna(subset=["Price","City"])
```

This ensures the dataset contains only valid property listings.

---

## 2.9 Return Clean Dataset

After cleaning the dataset, the function returns the cleaned DataFrame for use in the system.

---

## 2.10 Test Data Loading

To verify that the dataset loads correctly, a test script was created:

```
test.py
```

Example:

```python
from utils import load_data

df = load_data()

print(df.head())
```

This prints the first five rows of the dataset to confirm that the data was loaded successfully.

---

# 3. Stage 3 — Property Search Engine

## 3.1 Goal

Build the **core property search engine** that retrieves properties from the dataset using filters.

Instead of manually browsing thousands of rows, the system automatically filters properties based on conditions such as:

- City
- Bedrooms
- Maximum Price

---

## 3.2 Search Function

A function called `search_properties()` was implemented in:

```
utils.py
```

This function receives:

- the dataset (`df`)
- a dictionary of filters

Example filters:

```python
filters = {
    "city": "Nasr City",
    "bedrooms": 3,
    "max_price": 3000000
}
```

---

## 3.3 Filtering by City

The system filters properties by city using:

```python
results["City"].str.contains(filters["city"], case=False)
```

This allows flexible matching while ignoring letter case.

---

## 3.4 Filtering by Bedrooms

The system filters properties based on the requested number of bedrooms.

Example:

```python
results["Bedrooms"] == filters["bedrooms"]
```

---

## 3.5 Filtering by Maximum Price

Properties are filtered by maximum price:

```python
results["Price"] <= filters["max_price"]
```

---

## 3.6 Returning Results

To avoid returning too many rows, the system returns only the first 10 results.

Example:

```python
results.head(10)
```

---

## 3.7 Testing the Search Engine

The search engine was tested using:

```
test.py
```

Example:

```python
from utils import load_data, search_properties

df = load_data()

filters = {
    "city": "Nasr City",
    "bedrooms": 3,
    "max_price": 3000000
}

results = search_properties(df, filters)

print(results)
```

Running the test confirmed that the system correctly returns matching properties from the dataset.

---

## Stage 3 Result

The system can now:

- Load the dataset
- Apply property filters
- Retrieve matching listings from thousands of properties

---

# Current Progress

✔ Stage 1 — Project Setup  
✔ Stage 2 — Data Preparation  
✔ Stage 3 — Property Search Engine  

---

# Next Stage

# 4. Stage 4 — LLM Query Understanding

## 4.1 Goal

The goal of this stage is to enable the system to understand **natural language property search requests** and convert them into structured filters that can be used by the search engine.

Instead of forcing users to manually select filters like city, price, and bedrooms, users can now type natural language queries such as:

"Show me a 3 bedroom apartment in Nasr City under 3 million."

The system will analyze the request and automatically extract the required filters.

This step transforms the system from a simple search tool into an **AI-powered property assistant**.

---

## 4.2 LLM Provider

To understand user queries, the system integrates with a **Large Language Model (LLM)**.

For this project we used:

Groq API

Model used:

llama-3.1-8b-instant

Reasons for choosing this model:

- Free API access
- Very fast response time
- Good support for both Arabic and English
- Easy Python integration

---

## 4.3 LLM Integration

A new file was created in the project:

llm.py

This file is responsible for handling all communication with the LLM.

The system sends a carefully designed prompt to the model asking it to extract search filters from the user’s message.

The LLM then returns a structured JSON response containing the extracted filters.

---

## 4.4 Extract Filters Function

Inside `llm.py`, a function called:

extract_filters()

was implemented.

This function performs the following steps:

1. Receives the user's query in natural language
2. Sends the query to the LLM with a prompt
3. Requests the response in JSON format
4. Converts the JSON output into a Python dictionary

Example user query:

I want a 3 bedroom apartment in Nasr City under 3000000

Expected extracted filters:

{
  "city": "Nasr City",
  "bedrooms": 3,
  "max_price": 3000000
}

These filters are then passed to the search engine created in Stage 3.

---

## 4.5 Generating Conversational Responses

Another function was added:

generate_response()

This function uses the LLM to produce **natural conversational replies** based on the search results.

Instead of returning raw data from the dataset, the chatbot summarizes the results and communicates with the user in a friendly way.

Example response:

I found several apartments in Nasr City within your budget.
One of the best options is a 3-bedroom apartment with a good area and price close to your limit.
Would you prefer something ready to move or under construction?

---

## 4.6 Multilingual Support

The chatbot was designed to support **both Arabic and English**.

The prompt instructs the LLM to respond in the **same language used by the user**.

Examples:

User query in English:

I want an apartment in Nasr City under 3 million

Chatbot response:

I found several apartments in Nasr City within your budget.

User query in Arabic:

عايز شقة في مدينة نصر تحت ٣ مليون

Chatbot response:

وجدت لك عدة شقق في مدينة نصر ضمن الميزانية المحددة.

---

## 4.7 Testing the LLM Integration

The LLM functionality was tested using the file:

test.py

Example test query:

user_query = "I want a 3 bedroom apartment in Nasr City under 3000000"

The testing process confirmed that the system can:

1. Understand the user's request
2. Extract structured filters
3. Search the dataset
4. Generate a natural chatbot response

---

## Stage 4 Result

After completing this stage, the system can now:

✔ Understand natural language property search requests  
✔ Extract structured filters automatically  
✔ Search the dataset based on user intent  
✔ Generate conversational responses  
✔ Support both Arabic and English queries

The project has now evolved from a simple filter system into an **AI-powered real estate assistant**.