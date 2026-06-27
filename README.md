# 🏦 Loan Eligibility Prediction System

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B.svg)
![Flask](https://img.shields.io/badge/Flask-API-black.svg)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-ML-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 🌐 Live Application

The frontend user interface is fully deployed and accessible to the public. 

* **Live Demo:** [Smart Loan Risk Evaluator](https://loan-ui-dfbh.onrender.com/)
* **Hosting Platform:** Render (Free Tier)
* **Status:** Active

A machine learning–powered web application that predicts **loan eligibility and default risk** using customer financial and demographic information. The project follows a **microservices architecture**, where a **Streamlit frontend** communicates with a **Flask backend API** hosting a trained machine learning pipeline.

✔ Compared 3 machine learning models  
✔ Applied feature engineering and hyperparameter tuning  
✔ Achieved ROC-AUC of 0.7539 with tuned Logistic Regression  
✔ Built a complete Flask + Streamlit web application for loan eligibility prediction  
---

# 📌 Project Overview

Financial institutions need to evaluate loan applicants accurately while minimizing the risk of defaults. This project automates that process by analyzing applicant details and predicting whether an applicant is likely to default on a loan.

The application combines:

- 🧠 Machine Learning
- ⚙️ Flask REST API
- 🖥️ Streamlit Frontend
- 📊 Feature Engineering
- 🔍 Hyperparameter Tuning
- 🚀 End-to-End Deployment Ready Architecture

---

# 🚀 Key Features

- Predicts loan default risk in real time.
- User-friendly Streamlit web interface.
- Flask API for model inference.
- Automated preprocessing pipeline.
- Custom feature engineering.
- Hyperparameter tuning using `RandomizedSearchCV`.
- Handles categorical and numerical features seamlessly.
- Deployable as a standalone web application.

---

# 🤖 Machine Learning Pipeline

## Data Preprocessing

- Missing value handling
- Categorical encoding
- Numerical scaling
- Column transformations using Scikit-Learn pipelines

## Feature Engineering

The following custom features were created:

- ✅ `Income_Loan_Ratio`
- ✅ `Employment_Stability`
- ✅ `High_DTI_Flag`
- ✅ `credit_score_category`
- ✅ `log_income`
- ✅ `log_loan_amount`

These engineered features improved the predictive capability of the final model.

---

# 📈 Model Selection

Three machine learning models were evaluated: Logistic Regression, Random Forest, and XGBoost.

Although Random Forest achieved higher overall accuracy (87%), it struggled to identify loan defaults, achieving only 20% recall for the default class.

After comparing ROC-AUC, recall, and overall performance, Logistic Regression was selected as the final production model because it achieved the highest ROC-AUC (0.7539) and detected approximately 69% of default cases, making it more suitable for credit risk assessment.


| Model | ROC-AUC |
|--------|---------|
| Logistic Regression | **0.7539** ✅ |
| XGBoost | 0.7441 |
| Random Forest | 0.7311 |

After comparison, **Logistic Regression** was selected as the production model because it achieved the highest ROC-AUC score and provided strong, interpretable performance.

---

# 📊 Final Model Performance

## Logistic Regression (Hyperparameter Tuned)

| Metric | Score |
|----------|--------|
| ROC-AUC Score | **0.7539** |
| Accuracy | **68.62%** |
| Precision (Default Class) | **0.22** |
| Recall (Default Class) | **0.69** |
| F1-Score (Default Class) | **0.34** |

The model successfully identifies a significant proportion of risky loan applicants while maintaining competitive overall performance.

---

# 🛠️ Hyperparameter Tuning

Randomized Search Cross Validation was used to optimize the Logistic Regression model.

Best Parameters:

```python
{
    "C": 0.017638,
    "penalty": "l1",
    "solver": "saga",
    "max_iter": 1000
}
```

Cross Validation:

- 3-Fold Cross Validation
- 50 Random Parameter Combinations
- Optimization Metric: **ROC-AUC**

---

# 🏗️ System Architecture

```
                ┌──────────────────────┐
                │   Streamlit Frontend │
                │      (Port 8501)     │
                └──────────┬───────────┘
                           │
                    HTTP POST Request
                           │
                           ▼
                ┌──────────────────────┐
                │      Flask API       │
                │      (Port 5000)     │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │  ML Prediction Model │
                │ Logistic Regression  │
                └──────────┬───────────┘
                           │
                           ▼
                Loan Risk Prediction
```

---

# 📂 Project Structure

```text
Loan-Eligibility-Prediction/
│
├── app/
│   ├── api.py
│   ├── app.py
│   ├── main_ui.py
│   ├── tech_stack.py
│   └── about.py
│
├── src/
│   ├── train_model.py
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── loan_production_pipeline.pkl
│   └── __init__.py
│
├── data/
│   └── cleaned_data.csv
│
├── run.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 💻 Technologies Used

### Programming Language

- Python

### Machine Learning

- Scikit-Learn
- Logistic Regression
- RandomizedSearchCV

### Data Processing

- Pandas
- NumPy

### Backend

- Flask

### Frontend

- Streamlit

### Model Persistence

- Joblib

### Visualization

- Matplotlib (optional)

---

# ⚡ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Loan-Eligibility-Prediction.git

cd Loan-Eligibility-Prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

## Step 1: Train the model (if needed)

```bash
python src/train_model.py
```

This generates:

```
loan_production_pipeline.pkl
```

## Step 2: Start the Flask backend

```bash
python app/api.py
```

## Step 3: Launch the Streamlit frontend

```bash
streamlit run app/app.py
```

Open your browser at:

```
http://localhost:8501
```

---

# 📥 Example Input

| Feature | Example |
|----------|----------|
| Age | 35 |
| Income | 90000 |
| LoanAmount | 15000 |
| CreditScore | 780 |
| NumCreditLines | 5 |
| InterestRate | 7.5 |
| LoanTerm | 36 |
| DTIRatio | 0.25 |
| EmploymentType | Full-time |
| HasMortgage | Yes |
| LoanPurpose | Home |
| HasCoSigner | Yes |

---

# 🎯 Future Improvements

- SHAP-based model explanations
- Probability calibration
- Threshold optimization for different lending policies
- Cloud deployment (AWS, Azure, GCP)
- Docker support
- User authentication and loan history
- Continuous model retraining pipeline

---

# 👨‍💻 Author

**Kumar Shanu**

Machine Learning • Python • Data Science • Full Stack Development

---

# 📜 License

This project is licensed under the MIT License.