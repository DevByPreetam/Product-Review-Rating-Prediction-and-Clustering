import re
import html
import unicodedata
import pandas as pd
import nltk

from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag


# --------------------------------------------------
# 1. NLTK RESOURCE CHECK
# --------------------------------------------------

def download_nltk_resources():

    resources = {
        "corpora/stopwords": "stopwords",
        "corpora/wordnet": "wordnet",
        "corpora/omw-1.4": "omw-1.4",
        "taggers/averaged_perceptron_tagger_eng":
            "averaged_perceptron_tagger_eng"
    }

    for path, package in resources.items():

        try:
            nltk.data.find(path)

        except LookupError:
            nltk.download(package, quiet=True)


download_nltk_resources()


# --------------------------------------------------
# 2. STOPWORDS - PRESERVE NEGATIONS
# --------------------------------------------------

stop_words = set(stopwords.words("english"))

negation_words = {
    "no", "not", "nor", "never",
    "n't", "cannot", "can't", "couldn't",
    "didn't", "doesn't", "don't", "hadn't",
    "hasn't", "haven't", "isn't", "mightn't",
    "mustn't", "needn't", "shouldn't", "wasn't",
    "weren't", "won't", "wouldn't"
}

stop_words = stop_words - negation_words


# --------------------------------------------------
# 3. BASIC TEXT CLEANING
# --------------------------------------------------

def clean_review_text(text):

    if pd.isna(text):
        return ""

    text = str(text)

    text = html.unescape(text)

    text = unicodedata.normalize("NFKC", text)

    text = re.sub(r"<[^>]+>", " ", text)

    text = re.sub(
        r"https?://\S+|www\.\S+",
        " URL ",
        text,
        flags=re.IGNORECASE
    )

    text = re.sub(r"[\x00-\x1f\x7f]", " ", text)

    text = text.lower()

    text = re.sub(r"\s+", " ", text).strip()

    return text


# --------------------------------------------------
# 4. STOPWORD REMOVAL
# --------------------------------------------------

def remove_stopwords_preserve_negation(text):

    tokens = text.split()

    filtered_tokens = [
        word for word in tokens
        if word not in stop_words
    ]

    return " ".join(filtered_tokens)


# --------------------------------------------------
# 5. POS-AWARE LEMMATIZATION
# --------------------------------------------------

lemmatizer = WordNetLemmatizer()


def get_wordnet_pos(tag):

    if tag.startswith("J"):
        return wordnet.ADJ

    elif tag.startswith("V"):
        return wordnet.VERB

    elif tag.startswith("N"):
        return wordnet.NOUN

    elif tag.startswith("R"):
        return wordnet.ADV

    else:
        return wordnet.NOUN


def lemmatize_text(text):

    tokens = text.split()

    tagged_tokens = pos_tag(tokens)

    lemmatized_tokens = [
        lemmatizer.lemmatize(word, get_wordnet_pos(tag))
        for word, tag in tagged_tokens
    ]

    return " ".join(lemmatized_tokens)


# --------------------------------------------------
# 6. TITLE DUPLICATION CHECK
# --------------------------------------------------

def title_already_in_review(title, review):

    return bool(title) and title.lower() in review.lower()


# --------------------------------------------------
# 7. REMOVE EXPLICIT RATING MENTIONS
# --------------------------------------------------

rating_phrase_pattern = (
    r"\b(?:one|two|three|four|five|[1-5])"
    r"\s*-?\s*stars?\b"
)


def remove_rating_mentions(text):

    text = re.sub(
        rating_phrase_pattern,
        " ",
        text,
        flags=re.IGNORECASE
    )

    text = re.sub(r"\s+", " ", text).strip()

    return text


# --------------------------------------------------
# 8. FINAL MODEL TEXT PREPROCESSING
# --------------------------------------------------

def preprocess_review(review_text, review_title=""):

    title = clean_review_text(review_title)

    review = clean_review_text(review_text)

    # Avoid duplicate title
    if title_already_in_review(title, review):

        combined_text = review

    else:

        combined_text = (title + " " + review).strip()

    # Remove rating phrases
    combined_text = remove_rating_mentions(combined_text)

    # Remove punctuation except apostrophes
    combined_text = re.sub(
        r"[^\w\s']",
        " ",
        combined_text
    )

    combined_text = re.sub(
        r"\s+",
        " ",
        combined_text
    ).strip()

    # Remove stopwords
    combined_text = remove_stopwords_preserve_negation(
        combined_text
    )

    # Lemmatization
    final_text = lemmatize_text(combined_text)

    return final_text