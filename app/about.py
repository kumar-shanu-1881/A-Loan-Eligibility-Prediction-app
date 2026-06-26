import streamlit as st

st.title("👤 About the Developer")
st.markdown("---")

st.markdown("""
### Hi there! 👋

I am a **Computer Science Engineering student specializing in Artificial Intelligence and Machine Learning**. 
I build end-to-end data products, focusing on robust machine learning architectures, statistical model tuning, and scalable model deployment.

### 💼 Professional Experience & Certifications
* **Data Science Intern** | Worked on scalable text summarization suites using open-weight models and custom tokenization data loaders.
* **Oracle Cloud Infrastructure** | AI Foundations Associate Certified.

### 🌐 Let's Connect!
If you are looking for an ML Engineer who bridges the gap between clean data science and reliable web software, let's chat:
""")

# Interactive buttons for your professional profiles
col1, col2 = st.columns(2)
with col1:
    st.link_button("🚀 View My GitHub Profile", "https://github.com/") # Add your real GitHub link here
with col2:
    st.link_button("💼 Connect on LinkedIn", "https://linkedin.com/")   # Add your real LinkedIn link here

st.markdown("---")
st.caption("Developed as part of the Final Capstone Portfolio Project.")