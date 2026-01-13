import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sales Analysis Dashboard", layout="wide")

st.title("📊 Sales Analysis Results")

# ---- File selector ----
files = {
    "Client Status Analysis": "Client_Status_Analysis (3).xlsx",
    "Sales Analysis Results": "Sales_Analysis_Results (6).xlsx",
    "Advanced Sales Insights": "Advanced_Sales_Insights (3).xlsx",
    "SKU Analysis": "SKU_Analysis.xlsx"
}

selected_file = st.selectbox(
    "Select analysis to view:",
    list(files.keys())
)

# ---- Load Excel ----
@st.cache_data
def load_excel(file_path):
    return pd.read_excel(file_path)

df = load_excel(files[selected_file])

# ---- Display ----
st.subheader(selected_file)
st.dataframe(df, use_container_width=True)

# ---- Basic stats ----
st.subheader("Summary")
st.write(df.describe(include="all"))
