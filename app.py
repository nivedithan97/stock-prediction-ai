import streamlit as st
from data_fetcher import get_stock_data, fetch_dummy_news
from sentiment_analysis import analyze_sentiment
from summariser import summarize_news

st.title("Stock Analysis Dashboard")

ticker = st.text_input("Enter stock ticker (e.g., NVDA, AAPL):")

if ticker:
    # Stock prices
    high, low = get_stock_data(ticker)
    st.subheader(f"Stock Prices for {ticker}")
    st.write(f"**High (Today):** ${high}")
    st.write(f"**Low (Today):** ${low}")

    # News
    st.subheader("Related News")
    news = fetch_dummy_news(ticker)
    for item in news:
        st.write(f"- {item}")

    # Sentiment
    st.subheader("Sentiment Analysis")
    sentiment_results = analyze_sentiment(news)
    for r in sentiment_results:
        st.write(f"**{r['headline']}** → {r['sentiment']} (confidence: {r['confidence']})")

    # Summary
    st.subheader("GenAI News Summary")
    summary = summarize_news(news)
    st.write(summary)