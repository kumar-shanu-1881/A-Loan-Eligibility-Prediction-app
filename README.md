# 🏦 Smart Loan Risk Evaluator (Microservices Architecture)

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-API-lightgrey.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B.svg)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-Machine%20Learning-F7931E.svg)

A full-stack machine learning platform that assesses risk and predicts the likelihood of loan default in real time. The system was developed using a robust microservice architecture, with a front-end UI and a back-end machine learning inference engine.

## 🚀 Business Value & ML Performance

In financial data sets, class imbalance significantly impacts model accuracy. In this project, balanced recall and interpretability were valued more than raw, deceptive accuracy.

* **Final Model:** Logistic Regression (Tuned via RandomizedSearchCV)
* **Optimization Methodology:** Utilized `L1 (Lasso) Regularization` in order to mathematically remove noisy features, creating an interpretable model ready to go into banking.
* **Feature Engineering:** Created custom financial indicators such as `Income_Loan_Ratio`, `High_DTI_Flag`, and `Employment_Stability`.
* **Performance Metrics:**
  * **ROC-AUC Score:** `0.75`
  * **Class 1 (Default) Recall:** `69%` (Ability to catch the bad loans)
  * **Class 0 (Safe) Recall:** `68%` (Ability to approve profitable customers)

## 🏗️ System Architecture

This system operates using a two-server microservice architecture.

```text
[ Streamlit UI Frontend ] (