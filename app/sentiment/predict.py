def simple_sentiment_check(text: str):
    text = text.lower()

    positive_words = ["gain", "growth", "profit", "surge", "strong"]
    negative_words = ["loss", "fraud", "decline", "risk", "drop"]

    positive_score = sum(word in text for word in positive_words)
    negative_score = sum(word in text for word in negative_words)

    if positive_score > negative_score:
        return "positive"
    elif negative_score > positive_score:
        return "negative"
    return "neutral"