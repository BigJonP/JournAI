from transformers import pipeline

sentiment_pipeline = pipeline(
    "sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment-latest"
)
emotion_pipeline = pipeline(
    "text-classification", model="j-hartmann/emotion-english-distilroberta-base"
)
