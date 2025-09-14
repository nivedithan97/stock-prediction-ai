from transformers import pipeline

# importing the pipeline funtion from transformers library
# this is a BART model fine-tuned for summarization
summary_model = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_news(news_list):
    combined_text = " ".join(news_list)
    # This function takes a long piece of text as input and generates a shorter, concise summary.
    summary = summary_model(
        combined_text,
        max_length=60,
        min_length=25,
        do_sample=False
    )
    return summary[0]['summary_text']
