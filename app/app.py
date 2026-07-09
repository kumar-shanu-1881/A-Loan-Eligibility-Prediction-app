import streamlit as st
from woke_url import wake_url


#Trigger the wake-up call at the start of your UI code
backend_is_awake = wake_url()

#Optional: Show a friendly status indicator to the user
if not backend_is_awake:
    st.info("⏳ Connecting to the cloud inference engine... If this is the first load, the backend may take 30-40 seconds to wake up from sleep mode.")
else:
    st.sidebar.success("● Cloud API Connected")
    

# Page Configuration
st.set_page_config(
    page_title="Loan Risk Portal",
    page_icon="🏦",
    layout="wide"
)


st.markdown("""
    <style>
        /* Hide the Deploy button completely */
        .stAppDeployButton {
            display: none !important;
        }
    </style>
""", unsafe_allow_html=True)

#Declare ofavailable web sub-pages
predict_page = st.Page("main_ui.py", title="Risk Evaluator", icon="📊", default=True)
tech_page = st.Page("tech_stack.py", title="Tech Stack & System", icon="🛠️")
about_page = st.Page("about.py", title="About & Contact", icon="👤")

#  Sidebar Navigation Matrix
pg = st.navigation({
    "Core Application": [predict_page],
    "Documentation": [tech_page, about_page]
})

# Inject structural sidebar branding
st.sidebar.markdown("### 🏦 Axis Analytics")
st.sidebar.caption("v1.2.0 - Production Balanced Release")

# Execute the active page
pg.run()