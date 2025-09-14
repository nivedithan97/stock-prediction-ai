from transformers import pipeline
import streamlit as st

# Lazy load and cache the summarizer model
@st.cache_resource
def get_summarizer_pipeline():
    """
    Loads the summarization pipeline with a smaller model.
    Cached so it's only initialized once per session.
    """
    return pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_news_cached(news_list):
    """
    Summarizes a list of news headlines/articles using a cached Hugging Face model.
    """
    summarizer = get_summarizer_pipeline()
    combined_text = " ".join(news_list)
    summary = summarizer(
        combined_text,
        max_length=130,
        min_length=30,
        do_sample=False
    )
    return summary[0]['summary_text']