import streamlit as st
import requests


# Page Config 
st.set_page_config(page_title="Loan Default Predictor", page_icon="🏦", layout="centered")

st.title("🏦 Smart Loan Risk Evaluator")
st.markdown("Enter the applicant's financial details below to compute real-time default probability.")
st.markdown("---")

# User Input UI (This is where submit_button is defined!) 
with st.form("loan_application"):
    st.subheader("Financial Metrics")
    col1, col2 = st.columns(2)
    
    with col1:
        income = st.number_input("Annual Income ($)", min_value=0, value=65000, step=1000)
        loan_amount = st.number_input("Requested Loan Amount ($)", min_value=0, value=25000, step=1000)
        credit_score = st.slider("Credit Score", min_value=300, max_value=850, value=680)
        interest_rate = st.number_input("Interest Rate (%)", min_value=1.0, max_value=35.0, value=10.5)
        
    with col2:
        loan_term = st.selectbox("Loan Term (Months)", [12,18, 24,30, 36,42, 48,54, 60])
        dti_ratio = st.slider("Debt-to-Income Ratio (DTI)", 0.0, 1.0, 0.35)
        num_credit_lines = st.number_input("Open Credit Lines", min_value=0, max_value=20, value=4)
        months_employed = st.number_input("Months Employed", min_value=0, value=36)

    st.subheader("Demographics & Loan Details")
    col3, col4 = st.columns(2)
    
    with col3:
        age = st.number_input("Applicant Age", min_value=18, max_value=100, value=35)
        education = st.selectbox("Education Level", ["High School", "Bachelor's", "Master's", "PhD"])
        employment_type = st.selectbox("Employment Type", ["Full-time", "Part-time", "Self-employed", "Unemployed"])
        marital_status = st.selectbox("Marital Status", ["Single", "Married", "Divorced"])
        
    with col4:
        loan_purpose = st.selectbox("Loan Purpose", ["Home", "Auto", "Business", "Education", "Other"])
        has_mortgage = st.selectbox("Has Existing Mortgage?(any loan currently in operation)", ["No", "Yes"])
        has_dependents = st.selectbox("Has Dependents?", ["No", "Yes"])
        has_cosigner = st.selectbox("Has Co-Signer?(Loan Guranter)", ["No", "Yes"])

    # The button is created here!
    submit_button = st.form_submit_button(label="Analyze Application")

#Prediction Logic (Connects to Flask) 
if submit_button:
    # Package the UI inputs into a dictionary
    input_data = {
        "Age": age,
        "Income": income,
        "LoanAmount": loan_amount,
        "CreditScore": credit_score,
        "MonthsEmployed": months_employed,
        "NumCreditLines": num_credit_lines,
        "InterestRate": interest_rate,
        "LoanTerm": loan_term,
        "DTIRatio": dti_ratio,
        "EmploymentType": employment_type,
        "HasMortgage": has_mortgage,
        "LoanPurpose": loan_purpose,
        "HasCoSigner": has_cosigner
    }
    
    with st.spinner('Connecting to Flask Backend for Analysis...'):
        try:
            # Send the data to your Flask API
            flask_url = "http://127.0.0.1:5000/predict"
            response = requests.post(flask_url, json=input_data)
            
            if response.status_code == 200:
                result = response.json()
                prediction = result['prediction']
                probability = result['probability']
                
                # Display Results 
                st.markdown("---")
                st.subheader("Evaluation Verdict")
                
                if prediction == 1: 
                    st.error("❌ **Application Denied.** High probability of default detected.")
                    st.warning(f"**Risk Score:** {probability * 100:.3f}% chance of default.")
                    st.progress(probability)
                else:
                    st.success("✅ **Application Approved.** Customer shows strong financial stability.")
                    st.info(f"**Risk Score:** Only a {probability * 100:.3f}% chance of default.")
                    st.progress(probability)
            else:
                st.error(f"Backend Error: {response.json().get('error')}")
                
        except requests.exceptions.ConnectionError:
            st.error("🚨 Could not connect to the backend! Make sure your Flask API is running in another terminal window.")