from transformers import pipeline
import streamlit as st

# Lazy load and cache the sentiment analysis model
@st.cache_resource
def get_sentiment_pipeline():
    """
    Loads the sentiment analysis pipeline.
    Cached so it's only initialized once per session.
    """
    return pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def analyze_sentiment_cached(news_list):
    """
    Analyzes the sentiment of a list of news headlines.
    Returns a list of dicts with headline, sentiment label, and confidence score.
    """
    sentiment_model = get_sentiment_pipeline()
    sentiments = sentiment_model(news_list)
    
    results = []
    for headline, sentiment in zip(news_list, sentiments):
        results.append({
            "headline": headline,
            "sentiment": sentiment["label"],
            "confidence": round(sentiment["score"], 2)
        })
    return results
