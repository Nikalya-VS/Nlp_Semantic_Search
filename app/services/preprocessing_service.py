import re
import string

import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


class PreprocessingService:

    def __init__(self):

        self.stop_words = set(stopwords.words("english"))

        self.lemmatizer = WordNetLemmatizer()

    def clean_text(self, text):

        if pd.isna(text):
            return ""

        text = str(text).lower()

        text = re.sub(r"http\S+", "", text)

        text = re.sub(r"<.*?>", "", text)

        text = text.translate(
            str.maketrans("", "", string.punctuation)
        )

        words = text.split()

        words = [
            self.lemmatizer.lemmatize(word)
            for word in words
            if word not in self.stop_words
        ]

        return " ".join(words)

    def preprocess_dataframe(self, df):

        df["Clean Query"] = df["User Query"].apply(self.clean_text)

        df["Clean Title"] = df["Title"].apply(self.clean_text)

        df["Clean Content"] = df["Content"].apply(self.clean_text)

        return df

    def create_search_text(self, df):

        df["Search_Text"] = (
            df["Clean Query"].fillna("") + " " +
            df["Clean Title"].fillna("") + " " +
            df["Clean Content"].fillna("") + " " +
            df["Keywords"].fillna("")
        )

        return df