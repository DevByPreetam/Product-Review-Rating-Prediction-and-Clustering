import os
import joblib

from src.preprocessing.text_cleaning import preprocess_review


# Find project root directory
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)


# Model paths
MODEL_PATH = os.path.join(
    BASE_DIR, "models", "regression", "final_ridge_model.pkl"
)

VECTORIZER_PATH = os.path.join(
    BASE_DIR, "models", "regression", "final_tfidf_vectorizer.pkl"
)


# Load model and vectorizer only once
model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)


def predict_rating(review_text, review_title=""):
    """
    Predict product rating from raw customer review text.

    Parameters:
        review_text: Original customer review.
        review_title: Original review title (optional).

    Returns:
        Predicted rating between 1 and 5.
    """

    if not isinstance(review_text, str) or not review_text.strip():
        raise ValueError("Review text cannot be empty.")

    if not isinstance(review_title, str):
        raise ValueError("Review title must be a string.")

    # Preprocess raw review and title
    processed_text = preprocess_review(
        review_text=review_text,
        review_title=review_title
    )

    if not processed_text.strip():
        raise ValueError("Review contains no usable text after preprocessing.")

    # Convert processed text into TF-IDF features
    text_features = vectorizer.transform([processed_text])

    # Predict rating
    prediction = model.predict(text_features)[0]

    # Restrict rating to valid range
    prediction = max(1, min(5, prediction))

    return round(float(prediction), 2)