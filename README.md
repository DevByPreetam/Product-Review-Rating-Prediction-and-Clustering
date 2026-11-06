# Product Review Rating Prediction and Review Clustering

## 1. Project Overview

This project uses Natural Language Processing (NLP) and Machine Learning to analyse customer product reviews.

It consists of two major components:

**1. Supervised Learning – Rating Prediction**

Predict the numerical star rating of a product review based on its textual content using regression algorithms.

**2. Unsupervised Learning – Review Clustering**

Group similar product reviews to discover common customer opinions, product-related issues, and recurring themes.

## 2. Objectives

- Perform exploratory data analysis on product reviews.
- Clean and preprocess textual review data.
- Convert text into numerical representations using TF-IDF.
- Develop machine learning models for rating prediction.
- Cluster reviews using K-Means.
- Evaluate model performance and interpret discovered patterns.

## 3. Technology Stack

- Python
- Pandas and NumPy
- Scikit-learn
- NLTK
- Matplotlib and Seaborn
- Jupyter Notebook
- Git and GitHub

## 4. Project Methodology

### Module 1: Rating Prediction
- Linear Regression
- Ridge Regression
- Linear Support Vector Regression
- Evaluation using MAE, MSE, RMSE and R².

### Module 2: Review Clustering
- TF-IDF feature extraction
- Truncated SVD for dimensionality reduction
- K-Means clustering
- Elbow Method and Silhouette Score
- Cluster interpretation

## 5. Repository Structure

```text
Product-Review-Rating-Prediction-and-Clustering/
│
├── dataset/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│
├── src/
│   ├── preprocessing/
│   ├── features/
│   ├── prediction/
│   ├── clustering/
│   └── evaluation/
│
├── models/
├── visualizations/
├── results/
├── reports/
├── tests/
│
├── README.md
├── requirements.txt
└── .gitignore
```

## 6. Team Responsibilities

| Team Member | Responsibility |
|---|---|
| Ayushee Adyasha | Dataset inspection and EDA |
| Adyasha Panda | Text preprocessing and TF-IDF |
| Preetam Sahu | Rating prediction and model evaluation |
| Suhani Barik | Review clustering |

## 7. Installation

Clone the repository:

```bash
git clone <repository-url>
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 8. Project Status

Currently in the development phase.

Dataset selection, preprocessing, model development, evaluation and clustering will be documented as the project progresses.