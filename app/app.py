import streamlit as st
import requests

#live Render backend URL
BACKEND_URL = "https://loan-api-iuqc.onrender.com"

# cached function that pings the backend once on startup
@st.cache_resource(show_spinner=False)
def wake_up_backend():
    try:
        # A quick GET request to the backend's root or health endpoint
        # We set a short timeout so it doesn't freeze the frontend forever
        response = requests.get(BACKEND_URL, timeout=5)
        return True
    except requests.exceptions.RequestException:
        # If it times out or fails, it means the server is currently spinning up
        return False

#Trigger the wake-up call at the start of your UI code
backend_is_awake = wake_up_backend()

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