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
[ Streamlit UI Frontend ] (Port 8501)
         │
         ▼ (Encapsulated JSON Payload via HTTP POST)
 [ Flask API Backend ]    (Port 5000)
         │
         ▼ (Processes via Pipeline Engine)
[ Logistic Regression Pipeline (.pkl) ]

```


## 📂 Project Structure

Loan-Eligibility-Prediction/
├── app/
│   ├── api.py                   # ⚙️ Flask Backend (Listens for JSON payloads)
│   ├── app.py                   # 🖥️ Streamlit Master Navigation Router
│   ├── main_ui.py               # 📊 Core application layout & forms
│   ├── tech_stack.py            # 🛠️ System architecture documentation
│   └── about.py                 # 👤 Developer contact page
├── src/
│   ├── __init__.py              
│   ├── data_preprocessing.py    # Sklearn column transformers
│   ├── Feature_Engineering.py   # Custom ratio & flag generation
│   ├── train_model.py           # Factory script for hyperparameter tuning
│   └── loan_production_pipeline.pkl  # 🧠 Final trained Logistic Regression model
├── run.py                       # 🚀 Master startup script (Launches both servers)
├── requirements.txt             # Python dependencies
└── .gitignore                   # Keeps repository clean of data blobs



## 💻 How to Run locally

    1.Clone the Repository:
        git clone [https://github.com/your-username/A-Loan-Eligibility-Prediction-app.git](https://github.com/your-username/A-Loan-Eligibility-Prediction-app.git)
        cd A-Loan-Eligibility-Prediction-app
    
    2. Install dependencies
        pip install -r requirements.txt

    3. Launch the Microservices
        python run.py

    The web dashboard will automatically open in your default browser at http://localhost:8501.