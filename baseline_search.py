import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("semantic_search_preprocessed.csv")

df["Search_Text"] = (
    df["Clean Query"] + " " +
    df["Clean Title"] + " " +
    df["Clean Content"] + " " +
    df["Keywords"]
)

vectorizer = TfidfVectorizer(
    stop_words="english",
    ngram_range=(1,2),
    max_features=20000
)

document_vectors = vectorizer.fit_transform(df["Search_Text"])

query = input("Enter your search query: ")
query_vector = vectorizer.transform([query])

similarity_scores = cosine_similarity(
    query_vector,
    document_vectors
)

top_indices = similarity_scores[0].argsort()[-5:][::-1]

print("\nTop Results\n")

for idx in top_indices:

    print("=" * 70)

    print("Document ID :", df.iloc[idx]["Document ID"])

    print("Category :", df.iloc[idx]["Category"])

    print("Title :", df.iloc[idx]["Title"])

    print("Similarity :", similarity_scores[0][idx])

    print("Content :")

    print(df.iloc[idx]["Content"][:250], "...")

    print()