import pandas as pd
#load dataset
df = pd.read_csv("semantic_search_dataset.csv")

#No.of.columns and rows
print("=" * 50)
print("Dataset Shape")
print("=" * 50)
print(df.shape)

print("\n")

#column names
print("=" * 50)
print("Columns")
print("=" * 50)
print(df.columns)

print("\n")

#First five rows
print("=" * 50)
print("First Five Rows")
print("=" * 50)
print(df.head())

#missing values
print("=" * 50)
print("Missing Values")
print("=" * 50)
print(df.isnull().sum())

#Duplicate rows
print("=" * 50)
print("Duplicate Rows")
print("=" * 50)
print(df.duplicated().sum())

#unique_categories
print("=" * 50)
print("Unique Categories")
print("=" * 50)
print(df["Category"].nunique())
print(df["Category"].unique())

#category count
print("=" * 50)
print("Category Counts")
print("=" * 50)
print(df["Category"].value_counts())
df["Content Length"] = df["Content"].apply(len)
print(df["Content Length"].describe())
