import streamlit as st

st.title("🏦 About the Project")
st.markdown("---")

#Hero Section (The Elevator Pitch)
st.markdown("""
## 📌 Smart Loan Eligibility Prediction System

This project is an end-to-end machine learning microservice designed to estimate the likelihood of loan defaults based on financial and demographic data. 

The primary objective is to assist financial institutions in making **data-driven lending decisions**, balancing the need to approve profitable customers while mathematically shielding the bank from high-risk credit defaults.
""")

st.markdown("---")

# Modern UI: Using Tabs for Organization
tab1, tab2, tab3 = st.tabs(["🎯 Business Impact & Metrics", "🧠 ML Architecture", "🛠️ Tech Stack"])

# : Business Impact & Metrics 
with tab1:
    st.subheader("Measuring What Matters")
    st.markdown("In financial datasets, raw accuracy is often misleading due to class imbalance. This project prioritized **balanced recall** to ensure real-world business viability.")
    
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Final Production Model", value="Logistic Reg.", delta="Tuned via RandomizedSearchCV", delta_color="normal")
    col2.metric(label="ROC-AUC Score", value="0.75+", delta="Strong Class Separation", delta_color="normal")
    col3.metric(label="Architecture Pattern", value="Microservices", delta="Flask + Streamlit", delta_color="normal")

    with st.expander("💡 Why Logistic Regression over XGBoost?"):
        st.info("""
        While multiple algorithms (Random Forest, XGBoost) were evaluated, Logistic Regression was selected as the final production model. 
        
        In the banking sector, **interpretability** is mandated by law. Logistic Regression with L1 (Lasso) Regularization provides a clear mathematical explanation for every approval or denial, making it the superior choice for strict financial regulations over "black-box" tree models.
        """)

# ML Architecture 
with tab2:
    col_feat, col_flow = st.columns([1, 1.5])
    
    with col_feat:
        st.subheader("⚙️ Key Features")
        st.markdown("""
        * **Automated Feature Engineering:** Dynamically generates financial ratios (e.g., `Income_to_Loan`, `DTI_Flags`).
        * **Synthetic Balancing:** Mitigates severe dataset imbalance utilizing the **SMOTE** algorithm.
        * **REST API Decoupling:** Frontend and backend communicate exclusively via JSON payloads.
        """)
        
    with col_flow:
        st.subheader("🔄 The Data Pipeline")
        st.code("""
[ Raw Historical Loan Data ]
            │
[ Cleaning & Preprocessing ]
            │
[ Custom Feature Engineering ]
            │
[ SMOTE Class Balancing ]
            │
[ Hyperparameter Tuning (CV) ]
            │
[ Final Serialized Model (.pkl) ]
        """, language="text")

# --- TAB Tech Stack 
with tab3:
    st.subheader("🧰 Development Tools")
    
    stack_col1, stack_col2 = st.columns(2)
    with stack_col1:
        st.markdown("**Core Data Science:**")
        st.markdown("- 🐍 Python 3.10+")
        st.markdown("- 🐼 Pandas & NumPy")
        st.markdown("- 🤖 Scikit-Learn")
        st.markdown("- ⚖️ Imbalanced-Learn (SMOTE)")
        
    with stack_col2:
        st.markdown("**Deployment & Engineering:**")
        st.markdown("- ⚙️ Flask (Backend API)")
        st.markdown("- 🖥️ Streamlit (Frontend UI)")
        st.markdown("- 📦 Joblib (Serialization)")
        st.markdown("- 🔄 Requests (HTTP Routing)")

st.markdown("---")

#  Final Footer
st.caption(
    "This system showcases a complete lifecycle deployment: bridging the gap between exploratory data science "
    "and scalable, production-ready software engineering."
)