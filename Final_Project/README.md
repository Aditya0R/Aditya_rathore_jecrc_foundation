# 🚀 Lead Scoring Prediction System using Machine Learning

## 📌 Project Overview

The Lead Scoring Prediction System is a Machine Learning project developed to help sales teams identify and prioritize high-quality leads based on their likelihood of conversion.

The model predicts whether a lead is likely to become a paying customer and assigns a Lead Score (0–100). This enables organizations to focus on the most promising prospects, improving sales efficiency and increasing conversion rates.

---

# 📖 Problem Statement

X Education generates thousands of leads through multiple online marketing channels.

Currently,

- Every lead is treated equally.
- Sales representatives spend time on low-quality leads.
- Only around **30%** of leads convert into customers.

The objective of this project is to build a Machine Learning model capable of predicting whether a lead will convert into a customer and assigning a lead score to prioritize sales efforts.

---

# 🎯 Business Objective

The primary objectives are:

- Predict lead conversion using Machine Learning.
- Generate Lead Scores between 0 and 100.
- Classify leads into:
  - Hot Leads
  - Warm Leads
  - Cold Leads
- Help the sales team prioritize high-potential customers.
- Improve conversion rates while reducing sales effort.

---

# 📂 Dataset Information

Dataset Name:

**Lead Scoring Dataset**

Source:

X Education Lead Scoring Dataset

Dataset Size:

- Rows: 9,240
- Columns: 37

Target Variable:

```
Converted

1 → Converted

0 → Not Converted
```

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- Joblib
- Jupyter Notebook / Kaggle
- VS Code

---

# 📊 Project Workflow

```
Business Understanding
        ↓
Data Collection
        ↓
Data Cleaning
        ↓
Exploratory Data Analysis (EDA)
        ↓
Feature Engineering
        ↓
Data Preprocessing
        ↓
Encoding
        ↓
Feature Scaling
        ↓
Train-Test Split
        ↓
Model Building
        ↓
Model Evaluation
        ↓
Lead Score Generation
        ↓
Model Saving
```

---

# 🧹 Data Preprocessing

The following preprocessing steps were performed:

- Removed unnecessary ID columns.
- Removed constant-value columns.
- Handled missing values.
- Replaced invalid "Select" values.
- One-Hot Encoding for categorical features.
- Standard Scaling of numerical features.
- Train-Test Split (70:30).

---

# 📈 Exploratory Data Analysis

Performed extensive EDA including:

- Missing Value Analysis
- Target Variable Distribution
- Lead Source Analysis
- Lead Origin Analysis
- Occupation Analysis
- Country Analysis
- City Analysis
- Last Activity Analysis
- Correlation Heatmap
- Histogram
- Boxplots
- Feature Relationships

---

# 🤖 Machine Learning Models

The following models were trained and evaluated:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

The Random Forest model achieved the best overall performance and was selected as the final model.

---

# 📏 Evaluation Metrics

The following metrics were used:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC Score
- Confusion Matrix
- Classification Report

---

# 🎯 Lead Score Generation

The model predicts the probability of conversion.

Lead Score is calculated as:

```
Lead Score = Probability × 100
```

Example:

| Probability | Lead Score | Category |
|-------------|-----------|----------|
|0.95|95|Hot Lead|
|0.78|78|Warm Lead|
|0.22|22|Cold Lead|

---

# 📌 Lead Categories

| Lead Score | Category | Action |
|------------|----------|--------------------------|
|80 – 100|🔥 Hot Lead|Immediate Sales Call|
|60 – 79|🟡 Warm Lead|Email / Follow-up|
|Below 60|❄️ Cold Lead|Marketing Campaign|

---

# 📊 Business Recommendations

- Prioritize Hot Leads for immediate sales engagement.
- Assign Warm Leads to nurturing campaigns.
- Automate communication for Cold Leads.
- Continuously retrain the model with new customer data.
- Focus marketing efforts on high-converting lead sources.

---

# 📁 Project Structure

```
Lead-Scoring/

│── Lead_Scoring.ipynb

│── app.py

│── lead_scoring_model.pkl

│── scaler.pkl

│── lead_scores.csv

│── requirements.txt

│── README.md

│── images/

└── .gitignore
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/Lead-Scoring.git
```

Move into the project folder

```bash
cd Lead-Scoring
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 📷 Project Screenshots

Add screenshots here:

- Dataset Overview
- Missing Value Analysis
- Correlation Heatmap
- Confusion Matrix
- ROC Curve
- Feature Importance
- Lead Score Prediction

---

# 🚀 Future Improvements

- Streamlit Dashboard
- Flask REST API
- CRM Integration
- XGBoost & LightGBM Models
- Hyperparameter Optimization
- Real-Time Lead Scoring
- Cloud Deployment (AWS / Azure)
- Automated Model Retraining

---

# 📈 Results

- Successfully predicted lead conversion using Machine Learning.
- Generated Lead Scores between 0–100.
- Prioritized leads into Hot, Warm, and Cold categories.
- Improved decision-making for sales teams through predictive analytics.

---

# 👨‍💻 Author

**Aditya Rathore**

B.Tech Computer Science (AI)

Machine Learning & Data Science Enthusiast

GitHub: https://github.com/Aditya0R
