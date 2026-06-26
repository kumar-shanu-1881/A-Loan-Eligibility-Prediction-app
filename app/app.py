import streamlit as st

# Page Configuration
st.set_page_config(page_title="Loan Risk Portal", page_icon="🏦", layout="centered")

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