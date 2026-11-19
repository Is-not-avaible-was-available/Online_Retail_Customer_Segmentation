# Customer Segmentation Using Unsupervised Machine Learning
### An Analysis of Online Retail Transaction Data

## Project Overview

This project applies **unsupervised machine learning techniques** to identify meaningful customer segments based on purchasing behaviour, spending patterns and transaction frequency.

Using the UCI Online Retail dataset, the project transforms transaction-level data into customer-level behavioural features and applies clustering algorithms to identify distinct groups of customers.

The primary objective is to understand how customers differ in their purchasing patterns and demonstrate how data-driven segmentation can support customer engagement, retention and marketing strategies.

**Project:** Introduction to Machine Learning – Mini Project  
**Institution:** Tata Institute of Social Sciences (TISS), Mumbai  
**Programme:** School of Analytics  
**Machine Learning Task:** Unsupervised Learning – Clustering  
**Unit of Analysis:** Individual Customer  
**Dataset:** UCI Online Retail

---

## Research Problem

Online retailers serve customers with diverse purchasing behaviours. Some customers purchase frequently and contribute substantial revenue, while others make occasional purchases or become inactive over time.

Understanding these differences is important for developing effective customer engagement and retention strategies.

This project investigates whether unsupervised machine learning can identify meaningful customer segments using historical transaction data.

### Central Research Question

Can unsupervised machine learning identify meaningful customer segments based on purchasing behaviour, spending patterns and transaction frequency in an online retail business?

### Supporting Research Questions

1. What distinct customer segments can be identified using Recency, Frequency and Monetary (RFM) features?
2. How do these segments differ in purchasing behaviour, spending and product diversity?
3. Does incorporating additional behavioural features improve customer segmentation compared with traditional RFM-based clustering?
4. How do K-Means and Hierarchical Clustering compare in terms of cluster quality and interpretability?

---

## Dataset Description

The project uses the **UCI Online Retail Dataset**, which contains transactions from a UK-based online retail business between December 2010 and December 2011.

- **Source:** UCI Machine Learning Repository
- **Original observations:** 541,909 transaction records
- **Original variables:** 8
- **Time period:** December 2010 – December 2011

### Dataset Variables

| Variable | Description |
|---|---|
| InvoiceNo | Unique invoice or transaction identifier |
| StockCode | Product identifier |
| Description | Product description |
| Quantity | Number of units purchased |
| InvoiceDate | Date and time of transaction |
| UnitPrice | Price per unit |
| CustomerID | Unique customer identifier |
| Country | Country associated with the transaction |

**Dataset source:** [UCI Machine Learning Repository – Online Retail](https://archive.ics.uci.edu/dataset/352/online+retail)

The dataset contains missing customer identifiers, cancellations, returns and extreme transaction values. These characteristics were examined during data quality assessment and preprocessing.

---

## Methodology

The project follows a structured machine learning workflow.

### 1. Data Understanding and Exploratory Data Analysis

The initial analysis examines:

- Dataset structure and variable characteristics.
- Missing values and duplicate observations.
- Cancelled transactions and returns.
- Customer, invoice and product distributions.
- Transaction quantities and unit prices.
- Sales and purchasing patterns.

### 2. Data Preprocessing

The transaction-level dataset is cleaned and transformed into a customer-level analytical dataset.

Key preprocessing decisions include:

- Removing exact duplicate records.
- Identifying and excluding cancelled invoices from completed-purchase calculations.
- Excluding records without identifiable CustomerIDs from customer-level clustering.
- Retaining positive-quantity and positive-price purchase records.
- Excluding postage and non-merchandise stock codes from the primary merchandise analysis.
- Investigating extreme observations and conducting sensitivity analysis.

The original dataset is preserved separately from the processed analytical data.

### 3. Feature Engineering

Two feature sets are developed.

**A. RFM Features**

| Feature | Definition | Business Interpretation |
|---|---|---|
| Recency | Days since the customer's last purchase | Customer engagement |
| Frequency | Number of distinct completed invoices | Purchase frequency |
| Monetary | Total customer spending | Historical monetary contribution |

**B. Extended Behavioural Features**

In addition to RFM, the extended feature set includes:

- Average Order Value
- Total Quantity
- Product Diversity

Purchase Regularity was also calculated as a supplementary variable but excluded from clustering because it is structurally unavailable for customers with only one invoice.

### 4. Data Transformation and Scaling

The project examines:

- Logarithmic transformations to address skewness.
- Feature correlations and potential redundancy.
- StandardScaler and RobustScaler.
- Outlier sensitivity.
- Reduced extended feature sets.

No blanket removal of outliers was performed. Sensitivity analysis was used to examine the effect of selected extreme observations.

### 5. Clustering Models

Two clustering algorithms were evaluated.

| Model | Role |
|---|---|
| K-Means Clustering | Baseline model |
| Agglomerative Hierarchical Clustering | Comparison model |

Experiments were conducted using RFM and extended behavioural feature sets.

### 6. Model Evaluation

The following internal clustering evaluation metrics were used:

| Metric | Purpose | Preferred Direction |
|---|---|---|
| Silhouette Score | Measures cluster cohesion and separation | Higher |
| Davies-Bouldin Index | Measures similarity between clusters | Lower |
| Calinski-Harabasz Index | Evaluates between-cluster and within-cluster dispersion | Higher |

Additional validation included:

- Cluster size and proportion analysis.
- Customer-level cluster profiling.
- Repeated initialisation stability.
- Comparison of StandardScaler and RobustScaler.
- Outlier sensitivity analysis.
- Agreement between clustering partitions using Adjusted Rand Index (ARI).

---

## Key Findings

### Final Selected Model

The RFM-based K-Means model with three clusters was selected as the preferred model among the evaluated candidates.

| Evaluation Metric | Result |
|---|---:|
| Number of clusters | 3 |
| Silhouette Score | 0.4151 |
| Davies-Bouldin Index | 0.8269 |
| Calinski-Harabasz Index | 4,378.52 |
| Customers segmented | 4,335 |

### Identified Customer Segments

The final model identified three customer segments.

| Customer Segment | Customers | Percentage |
|---|---:|---:|
| Occasional Active | 2,025 | 46.71% |
| High-Value Active | 1,325 | 30.57% |
| Inactive / Lapsed | 985 | 22.72% |
| **Total** | **4,335** | **100%** |

### Customer Segment Interpretation

**1. Occasional Active Customers**

These customers demonstrate relatively recent but infrequent purchasing activity. They represent the largest segment and offer opportunities for increasing repeat purchases and product engagement.

**2. High-Value Active Customers**

These customers demonstrate higher purchase frequency, monetary contribution and product diversity. They represent an important customer group for retention, loyalty programmes and personalised engagement.

**3. Inactive / Lapsed Customers**

These customers exhibit longer periods since their last purchase, lower purchase frequency and comparatively lower historical spending. Targeted re-engagement campaigns may help explore opportunities for reactivation.

### Model Comparison

The RFM K-Means model achieved the strongest overall internal evaluation results among the six principal candidate models.

| Model | K | Silhouette | Davies-Bouldin | Calinski-Harabasz |
|---|---:|---:|---:|---:|
| RFM K-Means | 3 | **0.4151** | **0.8269** | **4,378.52** |
| RFM Hierarchical | 2 | 0.3965 | 0.8371 | 3,276.07 |
| RFM Hierarchical | 3 | 0.3956 | 0.8669 | 4,151.08 |
| Extended K-Means | 2 | 0.3511 | 1.0616 | 3,116.79 |
| Reduced Extended K-Means | 2 | 0.3360 | 1.1176 | 2,802.58 |
| Extended Hierarchical | 2 | 0.3237 | 1.0306 | 2,510.93 |

The extended feature sets did not improve the internal evaluation metrics in the experiments conducted. However, additional behavioural features were useful for interpreting the resulting customer segments.

*Note: Clustering metrics from different feature spaces should be interpreted cautiously because the dimensionality and underlying feature distributions differ.*

---

## Business Recommendations

The identified customer segments provide a basis for differentiated customer engagement strategies.

| Segment | Suggested Strategy |
|---|---|
| Occasional Active | Targeted cross-selling, personalised recommendations and repeat-purchase incentives |
| High-Value Active | Loyalty programmes, retention initiatives and personalised offers |
| Inactive / Lapsed | Win-back campaigns, targeted communication and reactivation incentives |

These recommendations represent potential business applications of the segmentation results. Their actual effectiveness would require further testing.

---

## Project Structure

```text
Online_Retail_Customer_Segmentation/
│
├── data/
│   ├── raw/
│   │   └── Online Retail.xlsx
│   ├── interim/
│   └── processed/
│
├── notebooks/
│   ├── 01_dataset_understanding.ipynb
│   ├── 02_data_quality_assessment.ipynb
│   ├── 03_exploratory_data_analysis.ipynb
│   ├── 04_data_preprocessing_feature_engineering.ipynb
│   ├── 05_kmeans_baseline.ipynb
│   └── 06_model_evaluation_interpretation.ipynb
│
├── src/
│   ├── __init__.py
│   ├── data_loading.py
│   ├── data_quality.py
│   └── eda.py
│
├── reports/
│   └── phase_2/
│       ├── figures/
│       └── tables/
│
├── outputs/
│
├── requirements.txt
└── README.md
```

---

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/Is-not-avaible-was-available/Online_Retail_Customer_Segmentation.git
```

### 2. Navigate to the project directory

```bash
cd Online_Retail_Customer_Segmentation
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Windows PowerShell**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Prepare the dataset

Download the Online Retail dataset from the UCI Machine Learning Repository and place the original Excel file at:

```text
data/raw/Online Retail.xlsx
```

If the dataset is excluded from Git because of its size, it must be downloaded separately.

### 6. Run the notebooks

Open the project in Jupyter Notebook or Visual Studio Code and execute the notebooks in the following order:

1. `01_dataset_understanding.ipynb`
2. `02_data_quality_assessment.ipynb`
3. `03_exploratory_data_analysis.ipynb`
4. `04_data_preprocessing_feature_engineering.ipynb`
5. `05_kmeans_baseline.ipynb`
6. `06_model_evaluation_interpretation.ipynb`

Run each notebook sequentially to maintain the intended analytical workflow and generate the required processed datasets and outputs.

---

## Limitations and Responsible Machine Learning

The findings should be interpreted in light of the following limitations:

1. **Dataset representativeness:** The dataset represents one online retailer and a historical period from 2010–2011. The findings may not generalise to other retailers or current purchasing environments.

2. **Geographical imbalance:** The customer base is heavily concentrated in the United Kingdom, limiting comparisons across smaller geographical markets.

3. **Feature selection:** Segmentation is based primarily on historical purchasing behaviour and does not incorporate customer demographics, preferences or other contextual factors.

4. **Influence of extreme observations:** Although transformations, scaling and sensitivity checks were conducted, distance-based clustering may still be influenced by extreme customer behaviour.

5. **Cluster interpretation:** Cluster names are analytical interpretations of observed purchasing patterns, not objectively predefined customer categories.

6. **Historical nature of the analysis:** The segmentation describes historical behaviour and does not predict future purchases, churn or customer transitions.

7. **Responsible use:** Customer identifiers are used for analytical aggregation. The resulting segments should support human decision-making rather than replace business judgement.

The analysis identifies behavioural similarities and associations; it does not establish causal relationships.

---

## Conclusion

This project demonstrates the application of unsupervised machine learning to customer segmentation using retail transaction data.

The RFM-based K-Means model identified three interpretable customer groups with distinct purchasing patterns. The analysis also demonstrated that traditional RFM features provided stronger internal clustering results than the extended feature sets evaluated.

The resulting segmentation offers a practical foundation for differentiated customer engagement, retention and reactivation strategies.

The project emphasises the importance of data preparation, feature engineering, model evaluation, interpretability and responsible use when applying machine learning to business problems.

---

## Technologies and Libraries

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- SciPy
- Scikit-learn
- Statsmodels
- Git and GitHub

---

## Acknowledgements

- **Dataset:** UCI Machine Learning Repository – Online Retail.
- **Institution:** Tata Institute of Social Sciences, Mumbai.
- **Programme:** School of Analytics.
- **Course:** Introduction to Machine Learning.

---

*This repository documents the academic mini-project, including the data preparation workflow, exploratory analysis, clustering experiments, model evaluation and interpretation of customer segments.*