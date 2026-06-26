import streamlit as st

st.title("🛠️ Project Tech Stack & Architecture")
st.markdown("This enterprise-grade application splits the layout into two specialized microservices.")

st.subheader("🏗️ Architectural Blueprint")
st.code("""
[ Streamlit UI Frontend ] (Port 8501)
         │
         ▼ (Encapsulated JSON Payload via HTTP POST)
 [ Flask API Backend ]    (Port 5000)
         │
         ▼ (Processes via Pipeline Engine)
[ Logistic Regression Math (.pkl) ]
""")

# Component Table
st.subheader("🧰 Core Components")
components = {
    "Layer": ["Frontend UI", "Backend API", "Machine Learning", "Data Engineering", "Sampling Engine"],
    "Technology Used": ["Streamlit", "Flask", "Scikit-Learn", "Pandas & NumPy", "Imbalanced-Learn (SMOTE)"],
    "Purpose": [
        "Interactive dashboard for bank managers to input loan profiles.",
        "Invisible microservice running a production web server to handle data traffic.",
        "Hyperparameter-tuned Logistic Regression with L1 (Lasso) Regularization.",
        "Calculates custom real-time ratios like Income-to-Loan and DTI flags.",
        "Over-samples the minority class during training to eliminate data imbalance."
    ]
}
st.table(components)