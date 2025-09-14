from transformers import pipeline

# Load once
sentiment_model = pipeline("sentiment-analysis")

def analyze_sentiment(news_list):
    results = []
    for headline in news_list:
        sentiment = sentiment_model(headline)[0]
        results.append({
            "headline": headline,
            "sentiment": sentiment["label"],
            "confidence": round(sentiment["score"], 2)
        })
    return results