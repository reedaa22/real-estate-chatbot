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

## Project Development Stages

## Project Roadmap

The project will be developed through the following stages:

1. Project Setup  
   Preparing the development environment, creating the GitHub repository, and organizing the project structure.

2. Data Preparation  
   Loading the real estate dataset, cleaning the data, and preparing it for processing.

3. Property Search Engine  
   Building the core filtering and search system that retrieves properties from the dataset.

4. LLM Query Understanding  
   Using an LLM (Large Language Model) to understand user requests and convert them into structured filters.

5. Chat Interface  
   Creating a chatbot interface where users can interact with the system.

6. Backend API  
   Building a backend API that allows the chatbot to communicate with external systems such as websites.

7. Website Integration  
   Connecting the chatbot to a real estate website so users can search properties directly.

8. System Improvements & Optimization  
   Improving search ranking, performance, and adding advanced AI features.
Currently we have completed **Stage 1 and Stage 2**.

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
Used for testing the data loading process.

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

# Current Progress

✔ Stage 1 — Project Setup  
✔ Stage 2 — Data Preparation  

---

# Next Stage

# 3. Stage 3 — Property Search Engine

## 3.1 Goal

The goal of this stage is to build the **core property search engine** that allows the system to retrieve properties from the dataset based on specific filters.

Instead of manually browsing thousands of rows in the dataset, the system can filter properties automatically based on conditions such as:

- City
- Number of Bedrooms
- Maximum Price

---

## 3.2 Search Function

A new function called `search_properties()` was implemented in:

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

The function then filters the dataset step-by-step.

---

## 3.3 Filtering by City

The system checks if a city filter exists and filters the dataset accordingly.

Example logic:

```python
results["City"].str.contains(filters["city"])
```

This allows flexible matching while ignoring case differences.

---

## 3.4 Filtering by Bedrooms

The system filters the dataset to include only properties with the requested number of bedrooms.

Example:

```python
results["Bedrooms"] == filters["bedrooms"]
```

---

## 3.5 Filtering by Maximum Price

The dataset is filtered to include only properties with price less than or equal to the requested maximum price.

Example:

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

The search engine was tested using the file:

```
test.py
```

Example test:

```python
filters = {
    "city": "Nasr City",
    "bedrooms": 3,
    "max_price": 3000000
}
```

Running the test confirmed that the system correctly returns matching properties from the dataset.

---

## Stage 3 Result

The system can now:

- Load the dataset
- Apply search filters
- Retrieve matching properties from thousands of listings