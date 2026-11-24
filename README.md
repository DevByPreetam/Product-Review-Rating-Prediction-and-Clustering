# Product Review Rating Prediction and Review Clustering

## 1. Project Overview

This project uses Machine Learning and Natural Language Processing (NLP) to analyze product reviews.

It has two main objectives:

1. **Product Rating Prediction:** Predict a numerical product rating (1–5) based on the review text using regression algorithms.
2. **Review Clustering:** Group similar product reviews into clusters using unsupervised machine learning.

The project also provides simple terminal-based applications that allow users to enter reviews and receive predictions.

## 2. Project Objectives

- Preprocess and clean product review text.
- Convert textual reviews into numerical features using TF-IDF.
- Train and evaluate multiple regression models.
- Predict product ratings from review text.
- Group similar reviews using K-Means clustering.
- Evaluate clustering quality using the Elbow Method and Silhouette Score.
- Provide user-input applications for rating prediction and review clustering.

## 3. Technologies Used

- Python
- NumPy
- Pandas
- Scikit-learn
- NLTK
- Matplotlib
- Seaborn
- SciPy
- Joblib
- Jupyter Notebook
- Git and GitHub

## 4. Project Structure

```text
Product-Review-Rating-Prediction-and-Clustering/
│
├── dataset/
│   ├── raw/
│   └── processed/
│
├── models/
│   ├── clustering/
│   └── regression/
│
├── notebooks/
│
├── results/
│   └── clustering/
│
├── src/
│   ├── clustering/
│   │   └── kmeans.py
│   │
│   ├── evaluation/
│   │   └── metrics.py
│   │
│   ├── features/
│   │   └── tfidf.py
│   │
│   ├── prediction/
│   │   └── regression.py
│   │
│   └── preprocessing/
│       └── text_cleaning.py
│
├── tests/
│
├── visualizations/
│
├── predict_review.py
├── cluster_review.py
├── requirements.txt
└── README.md
```

## 5. Data Preprocessing

The review dataset is processed using NLP techniques.

The preprocessing pipeline includes:

- Removing unnecessary characters and noise.
- Text normalization.
- Tokenization.
- Stopword removal while preserving negation.
- Lemmatization.
- Combining review titles and review text where applicable.

The cleaned reviews are converted into numerical representations using TF-IDF.

## 6. Rating Prediction – Regression

The rating prediction component uses TF-IDF features and regression algorithms to estimate product ratings.

### Feature Extraction

TF-IDF configuration:

- Maximum features: 15,000
- N-gram range: (1, 3)

### Models Evaluated

- Linear Regression
- Ridge Regression
- ElasticNet Regression
- Linear SVR

### Final Model

**Ridge Regression** was selected as the final model based on its overall evaluation performance.

Final evaluation results:

| Metric | Result |
|---|---:|
| MAE | 0.3318 |
| MSE | 0.2391 |
| RMSE | 0.4889 |
| R² Score | 0.7265 |

The model achieved an R² score of approximately 0.73 on the test dataset.

These metrics measure prediction performance; R² is not classification accuracy.

### Saved Model Files

- `final_ridge_model.pkl`
- `final_tfidf_vectorizer.pkl`
- `model_info.json`

## 7. Review Clustering – K-Means

The clustering component groups similar product reviews without requiring predefined labels.

### Methodology

1. Convert review text into TF-IDF features.
2. Apply Truncated SVD for dimensionality reduction.
3. Use the Elbow Method to examine different cluster counts.
4. Evaluate clustering using Silhouette Scores.
5. Apply K-Means clustering.

### Configuration

| Parameter | Value |
|---|---:|
| TF-IDF Maximum Features | 5,000 |
| N-gram Range | (1, 2) |
| SVD Components | 100 |
| Selected Clusters | 3 |

### Clustering Results

| Cluster | Number of Reviews | Percentage |
|---|---:|---:|
| Cluster 0 | 1,828 | 6.46% |
| Cluster 1 | 8,107 | 28.64% |
| Cluster 2 | 18,376 | 64.91% |

The clusters represent groups of similar reviews. Their IDs do not represent ratings or sentiment labels.

The approximate themes identified include general positive/value feedback, battery/performance-related feedback, and miscellaneous product experiences.

The selected K-Means configuration achieved a sampled Silhouette Score of approximately 0.0695. This indicates limited separation between clusters, so the results should be interpreted as exploratory groupings.

### Saved Model Files

- `tfidf_vectorizer.pkl`
- `svd_model.pkl`
- `kmeans_model.pkl`
- `clustering_info.json`

## 8. Running the Applications

### Requirements

Install the required dependencies:

```bash
py -3.14 -m pip install -r requirements.txt
```

### A. Product Rating Prediction

Run:

```bash
py -3.14 predict_review.py
```

Enter a product review when prompted.

Example:

```text
Enter your product review:
Amazing product! Excellent quality and performance.

Predicted Rating: 4.82 / 5
```

Type `exit` to close the application.

### B. Product Review Clustering

Run:

```bash
py -3.14 cluster_review.py
```

Enter a product review.

Example:

```text
Enter your product review:
Excellent battery life and long lasting performance.

Predicted Cluster: 1
```

Type `exit` to close the application.

## 9. Evaluation Methods

### Regression Evaluation

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score
- Residual Analysis

### Clustering Evaluation

- Elbow Method
- Silhouette Score
- Cluster Distribution Analysis
- Cluster Interpretation

## 10. Future Enhancements

- Develop a web-based user interface.
- Improve clustering quality through alternative algorithms and feature representations.
- Explore advanced NLP techniques and transformer-based models.
- Incorporate product categories and additional review metadata.
- Improve model generalization using larger and more diverse datasets.

## 11. Conclusion

This project demonstrates how Machine Learning and NLP can be applied to product review analysis.

The regression component predicts numerical ratings from review text, while the clustering component discovers groups of similar reviews.

Together, these components provide a foundation for automated product review analysis and customer feedback understanding.

## 12. Contributors

**Team A2**

Product Review Rating Prediction and Review Clustering