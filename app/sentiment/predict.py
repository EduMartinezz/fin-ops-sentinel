from app.sentiment.model import get_finbert, get_finbert_error


def simple_sentiment_check(text: str):
    text = text.lower()

    positive_words = ["gain", "growth", "profit", "surge", "strong"]
    negative_words = ["loss", "fraud", "decline", "risk", "drop"]

    positive_score = sum(word in text for word in positive_words)
    negative_score = sum(word in text for word in negative_words)

    if positive_score > negative_score:
        return "positive", None, "rule_based"
    elif negative_score > positive_score:
        return "negative", None, "rule_based"
    return "neutral", None, "rule_based"


def finbert_sentiment_check(text: str):
    classifier = get_finbert()

    if classifier is None:
        error = get_finbert_error()
        if error:
            print(f"Using fallback sentiment because FinBERT is unavailable: {error}")
        return simple_sentiment_check(text)

    try:
        result = classifier(text)[0]
        return result["label"].lower(), float(result["score"]), "finbert"
    except Exception as e:
        print(f"FinBERT inference failed: {e}")
        return simple_sentiment_check(text)