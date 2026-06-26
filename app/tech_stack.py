import streamlit as st
import pandas as pd

# Page Configuration

st.title("🛠️ Technology Stack & System Architecture")
st.markdown("---")

st.markdown("""
This Loan Eligibility Prediction System is built as an **end-to-end machine learning application**
that combines data preprocessing, feature engineering, model inference, and a user-friendly web
interface to provide real-time loan risk predictions.
""")


# System Architecture

st.subheader("🏗️ System Architecture")

st.code("""
                ┌───────────────────────────┐
                │     Streamlit Frontend     │
                │  (User Input Dashboard)    │
                └─────────────┬──────────────┘
                              │
                 Applicant Information
                              │
                              ▼
                ┌───────────────────────────┐
                │      Flask REST API        │
                │    Prediction Endpoint     │
                └─────────────┬──────────────┘
                              │
                     Input Validation
                              │
                              ▼
                ┌───────────────────────────┐
                │ Feature Engineering Layer  │
                │ + Data Preprocessing       │
                └─────────────┬──────────────┘
                              │
                              ▼
                ┌───────────────────────────┐
                │ Logistic Regression Model  │
                │ (Serialized with Joblib)   │
                └─────────────┬──────────────┘
                              │
                              ▼
                   Loan Risk Prediction
""", language="text")

st.info(
    "The frontend is separated from the prediction engine, making the application modular, "
    "maintainable, and easier to deploy."
)


# Technology Stack

st.subheader("💻 Technology Stack")

tech_df = pd.DataFrame({
    "Component": [
        "Frontend",
        "Backend API",
        "Machine Learning",
        "Data Processing",
        "Feature Engineering",
        "Class Balancing",
        "Hyperparameter Tuning",
        "Model Persistence",
        "Visualization"
    ],
    "Technology": [
        "Streamlit",
        "Flask",
        "Scikit-Learn (Logistic Regression)",
        "Pandas & NumPy",
        "Custom Python Functions",
        "SMOTE (Imbalanced-Learn)",
        "RandomizedSearchCV",
        "Joblib",
        "Matplotlib & Seaborn"
    ],
    "Purpose": [
        "Interactive user interface for loan prediction.",
        "REST API serving prediction requests.",
        "Classifies applicants as low or high risk.",
        "Data manipulation and numerical computations.",
        "Creates financial indicators and derived features.",
        "Handles class imbalance during model training.",
        "Optimizes model parameters using cross-validation.",
        "Saves and loads trained ML pipelines efficiently.",
        "Supports exploratory data analysis and reporting."
    ]
})

st.dataframe(
    tech_df,
    use_container_width=True,
    hide_index=True
)


# ML Pipeline

st.subheader("🧠 Machine Learning Pipeline")

st.markdown("""
1. Load historical loan dataset.
2. Perform feature engineering.
3. Apply preprocessing (encoding and scaling).
4. Split data into training and testing sets.
5. Balance training data using SMOTE.
6. Train a Logistic Regression classifier.
7. Tune hyperparameters with RandomizedSearchCV.
8. Evaluate using ROC-AUC, Precision, Recall, F1-Score, and Accuracy.
9. Save the final pipeline using Joblib.
10. Load the trained pipeline inside the web application for real-time inference.
""")


# Key Features

st.subheader("🚀 Key Features")

col1, col2 = st.columns(2)

with col1:
    st.success("""
    ✅ Real-time loan prediction

    ✅ Automated feature engineering

    ✅ Hyperparameter-tuned ML model

    ✅ Handles class imbalance with SMOTE

    ✅ Serialized production pipeline
    """)

with col2:
    st.success("""
    ✅ REST API integration

    ✅ Modular project architecture

    ✅ Interactive Streamlit dashboard

    ✅ Reproducible preprocessing pipeline

    ✅ Ready for deployment
    """)


# Model Summary

st.subheader("📊 Final Model Summary")

st.metric("Selected Model", "Logistic Regression")
st.metric("ROC-AUC Score", "0.7539")
st.metric("Primary Objective", "Identify Potential Loan Defaults")

st.caption(
    "The final model was selected after comparing Logistic Regression, "
    "Random Forest, and XGBoost. Logistic Regression achieved the best "
    "ROC-AUC score while providing balanced performance for loan risk prediction."
)