import streamlit as st

# Import lightweight modules first
from data_fetcher import get_stock_data, fetch_dummy_news

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

    # Lazy load sentiment analysis
    st.subheader("Sentiment Analysis")
    if st.button("Analyze Sentiment"):
        from sentiment_analysis import analyze_sentiment  # delayed import
        sentiment_results = analyze_sentiment(news)
        for r in sentiment_results:
            st.write(f"**{r['headline']}** → {r['sentiment']} (confidence: {r['confidence']})")

    # Lazy load summarizer
    st.subheader("GenAI News Summary")
    if st.button("Summarize News"):
        from summariser import summarize_news  # delayed import
        summary = summarize_news(news)
        st.write(summary)
