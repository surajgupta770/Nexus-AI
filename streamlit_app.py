import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Nexus Insight Engine", layout="wide")

st.title("🚀 Nexus Insight Engine: Business AI")
st.write("Apni data file upload karein aur AI se analysis karwayein.")

# Sidebar for Monetization/Admin
st.sidebar.header("Premium Features")
st.sidebar.info("₹1000/day strategy: Offer this tool to local shops for data management.")

# File Uploader
uploaded_file = st.file_uploader("Excel ya CSV file yahan daalein", type=["csv", "xlsx"])

if uploaded_file:
    df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith('.csv') else pd.read_excel(uploaded_file)
    
    st.subheader("📊 Aapka Data Dashboard")
    st.dataframe(df.head())

    # Auto-Charts
    st.subheader("📈 Quick Analysis")
    column = st.selectbox("Kis column ka graph dekhna hai?", df.columns)
    fig = px.histogram(df, x=column, title=f"{column} ka Distribution")
    st.plotly_chart(fig)

    # AI Business Logic (Placeholder for Gemini)
    if st.button("Generate Business Growth Report"):
        st.success("Analyzing... Yeh feature aapke premium users ke liye ₹49/report ho sakta hai!")
