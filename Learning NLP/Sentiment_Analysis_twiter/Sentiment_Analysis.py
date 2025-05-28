import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

from nltk.sentiment import SentimentIntensityAnalyzer
from tqdm import tqdm
import nltk

# Load the dataset
df = pd.read_csv('Learning NLP/Sentiment_Analysis_twiter/Sentiment.csv')

# Drop the columns with too many missing values
drop_features = [col for col in df.columns if df[col].isnull().sum() > 10000]
drop_features = drop_features + ["thumbnail","quote_url","created_at","id","timezone"]

df = df.drop(columns=drop_features).reset_index()

# Apply the sentiment analysis using NLTK's SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()
res = {}
for i, row in tqdm(df.iterrows(), total=len(df)):
    text = row["tweet"]
    my_id = row["index"]
    res[my_id] = sia.polarity_scores(text)

# Convert the results into a DataFrame, compounding the scores into a single row per tweet
Results = pd.DataFrame(res).T
Results = Results.reset_index().rename({"index" : "Id"})
Results = Results.merge(df, how = "left")

# Check twiter sentiment
def detect_stance(text, compound):
    text_lower = text.lower()

    russia = "russia" in text_lower or "russian" in text_lower
    ukraine = "ukraine" in text_lower

    if compound >= 0.05:
        if russia:
            return "Pro-Russia"
        elif ukraine:
            return "Pro-Ukraine"
    elif compound <= -0.05:
        if russia:
            return "Anti-Russia"
        elif ukraine:
            return "Anti-Ukraine"
    
    return "Neutral"

# Apply the logic to detect stance
Results["stance"] = Results.apply(lambda row: detect_stance(row["tweet"], row["compound"]), axis=1)

print(Results["stance"].value_counts())
