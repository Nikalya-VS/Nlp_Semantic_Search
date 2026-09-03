import pandas as pd
import re

df = pd.read_csv("semantic_search_dataset.csv")

def clean_text(text):

    text = text.lower()

    text = re.sub(r"http\S+", "", text)

    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)

    text = re.sub(r"\s+", " ", text)

    return text.strip()

df["Clean Query"] = df["User Query"].apply(clean_text)

df["Clean Title"] = df["Title"].apply(clean_text)

df["Clean Content"] = df["Content"].apply(clean_text)

df.to_csv("semantic_search_preprocessed.csv", index=False)

print(df.head())