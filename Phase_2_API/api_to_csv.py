import requests
import pandas as pd

# API endpoint
url = "https://jsonplaceholder.typicode.com/users"

# API call
response = requests.get(url)

# Check if request was successful
response.raise_for_status()

# Convert JSON response to Python object
data = response.json()

# Flatten nested JSON
df = pd.json_normalize(data)

# Display data
print(df)

# Export to CSV
df.to_csv("api_users.csv", index=False)

print("\nCSV file created successfully: api_users.csv")

# Basic Data Analysis

print("\n--- Dataset Shape ---")
print(df.shape)

print("\n--- Column Names ---")
print(df.columns.tolist())

print("\n--- Data Types ---")
print(df.dtypes)

print("\n--- Missing Values ---")
print(df.isnull().sum())

print("\n--- First 5 Records ---")
print(df.head())

print("\n--- Number of Unique Cities ---")
print(df["address.city"].nunique())

print("\n--- Users by City ---")
print(df["address.city"].value_counts())

print("\n--- Companies ---")
print(df["company.name"].value_counts())