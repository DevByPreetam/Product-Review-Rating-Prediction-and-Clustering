# Dataset Summary and Exploratory Data Analysis

## 1. Dataset Information

**Dataset Name:** Datafiniti Amazon Product Consumer Reviews

**Original Dataset Dimensions:** 28,332 records × 24 columns

**Dataset Description:**

The dataset contains consumer reviews of Amazon products, along with ratings and product-related information.

The main fields used in this project are:

- `reviews.text`: The content of the customer review.
- `reviews.rating`: The rating given by the customer, ranging from 1 to 5.
- `reviews.title`: The title of the review.
- `name`: The product name.
- `brand`: The product brand.
- `categories`: The product category.

The dataset is used for product review rating prediction and review clustering.

## 2. Data Quality Analysis

### Missing Values

Missing values were examined across all columns.

The following columns had more than 50% missing values:

- `reviews.didPurchase`
- `reviews.id`
- `reviews.doRecommend`
- `reviews.numHelpful`

These columns were excluded from the separate cleaned DataFrame used for exploratory analysis.

The original dataset was preserved without modification.

The important review text and rating columns did not contain missing values in the initial dataset inspection.

### Duplicate Records

The dataset contained no exact duplicate rows.

However, repeated review texts were identified:

- Repeated review text occurrences: 10,164
- Groups of repeated review texts: 6,971
- Groups with consistent ratings: 6,853
- Groups with conflicting ratings: 118

Repeated review texts were retained during dataset preparation because identical review text does not necessarily indicate an invalid or duplicate record.

## 3. Rating Distribution

The rating column contains values ranging from 1 to 5.

| Rating | Number of Reviews | Percentage |
|---|---:|---:|
| 1 star | 965 | 3.41% |
| 2 stars | 616 | 2.17% |
| 3 stars | 1,206 | 4.26% |
| 4 stars | 5,648 | 19.93% |
| 5 stars | 19,897 | 70.23% |

### Observation

The dataset is strongly imbalanced towards 5-star reviews, which account for approximately 70.23% of all records.

This imbalance may affect rating prediction models, particularly when predicting lower ratings.

## 4. Review Length Analysis

Review lengths were analysed by calculating the number of words in each review.

The analysis included:

- Mean review length
- Median review length
- Minimum and maximum review length
- Standard deviation
- Review length distribution using a histogram
- Outlier examination using a boxplot

Detailed statistics and visualizations are available in the EDA notebook.

## 5. Frequent Word Analysis

Frequent words were identified after converting review text to lowercase, removing punctuation and excluding common stopwords.

The most frequent words were:

| Word | Frequency |
|---|---:|
| great | 9,464 |
| batteries | 8,145 |
| tablet | 6,685 |
| good | 5,906 |
| price | 5,221 |
| use | 4,484 |
| amazon | 3,918 |
| love | 3,549 |
| bought | 3,186 |
| easy | 2,954 |
| kindle | 2,886 |
| just | 2,819 |
| long | 2,514 |
| kids | 2,510 |
| like | 2,503 |
| work | 2,370 |
| buy | 2,276 |
| loves | 2,211 |
| old | 2,136 |
| battery | 2,132 |

### Observation

Words such as "great", "good", and "love" suggest generally positive customer feedback.

Product-related terms such as "batteries", "tablet", and "kindle" indicate recurring product topics in the reviews.

## 6. Dataset Preparation and Standardization

A standardized dataset was prepared for use by the other project members.

The following six columns were selected:

| Standardized Column | Original Column |
|---|---|
| `review_text` | `reviews.text` |
| `rating` | `reviews.rating` |
| `review_title` | `reviews.title` |
| `product_name` | `name` |
| `brand` | `brand` |
| `category` | `categories` |

### Review Text Validation

Empty, missing, and whitespace-only review texts were identified.

Records without usable review text were removed because they cannot be used for text-based prediction or clustering.

Missing values in optional metadata fields, such as review title, product name, brand, and category, were retained to avoid unnecessary loss of valid review records.

Repeated review texts were not removed.

### Record Retention

| Description | Number of Records |
|---|---:|
| Original records | 28,332 |
| Records retained | 28,332 |
| Records removed | 0 |

The retained and removed counts will be updated using the final dataset preparation output.

### Processed Dataset

The standardized dataset was saved as:

`dataset/processed/standardized_reviews.csv`

The original dataset was preserved without modification.

## 7. Key Findings

1. The dataset contains 28,332 customer reviews and 24 original columns.
2. The rating distribution is highly imbalanced, with 5-star reviews forming approximately 70.23% of the dataset.
3. No exact duplicate rows were found, although repeated review texts were present.
4. A total of 118 repeated review text groups had conflicting ratings.
5. Frequent-word analysis showed that positive expressions and product-related terms occur frequently.
6. The dataset was standardized into six relevant columns for downstream modelling.
7. Repeated review texts were retained, and only records without usable review text were removed during preparation.

## 8. Conclusion

The exploratory data analysis provided an understanding of the dataset's structure, missing values, repeated reviews, rating distribution, review lengths, and frequently occurring words.

A standardized dataset containing review text, rating, review title, product name, brand, and category was prepared for the subsequent stages of the project.

The processed CSV will serve as the common dataset for rating prediction and review clustering.