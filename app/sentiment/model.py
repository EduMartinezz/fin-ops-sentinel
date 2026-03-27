_finbert_pipeline = None
_finbert_error = None


def preload_finbert():
    global _finbert_pipeline, _finbert_error

    if _finbert_pipeline is not None:
        return _finbert_pipeline

    try:
        import torch
        from transformers import pipeline

        print(f"PyTorch version: {torch.__version__}")

        _finbert_pipeline = pipeline(
            "sentiment-analysis",
            model="ProsusAI/finbert",
            device=-1
        )
        _finbert_error = None
        print("FinBERT loaded successfully.")
        return _finbert_pipeline

    except Exception as e:
        _finbert_pipeline = None
        _finbert_error = str(e)
        print(f"FinBERT preload failed: {e}")
        return None


def get_finbert():
    return _finbert_pipeline


def get_finbert_error():
    return _finbert_error