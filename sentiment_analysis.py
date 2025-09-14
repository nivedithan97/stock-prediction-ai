from transformers import pipeline

# Load once
sentiment_model = pipeline("sentiment-analysis")

def analyze_sentiment(news_list):
    results = []
    # analyze the sentiment of a given text (e.g., a headline) and classify it as either positive, negative, or sometimes neutral
    sentiments = sentiment_model(news_list)
    for headline, sentiment in zip(news_list, sentiments):
        results.append({
            "headline": headline,
            "sentiment": sentiment["label"],
            "confidence": round(sentiment["score"], 2)
        })
    return results