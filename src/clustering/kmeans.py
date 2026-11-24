import os
import joblib

# Project root directory
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

MODEL_DIR = os.path.join(BASE_DIR, "models", "clustering")

# Load saved models
tfidf = joblib.load(
    os.path.join(MODEL_DIR, "tfidf_vectorizer.pkl")
)

svd = joblib.load(
    os.path.join(MODEL_DIR, "svd_model.pkl")
)

kmeans = joblib.load(
    os.path.join(MODEL_DIR, "kmeans_model.pkl")
)


def predict_cluster(review_text):
    """
    Predict the cluster for a preprocessed review.
    """

    if not isinstance(review_text, str) or not review_text.strip():
        raise ValueError("Review text cannot be empty.")

    tfidf_features = tfidf.transform([review_text])
    svd_features = svd.transform(tfidf_features)

    cluster = kmeans.predict(svd_features)

    return int(cluster[0])