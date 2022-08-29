import streamlit as st
import pandas as pd
from openpyxl import load_workbook

st.set_page_config(page_title="PKR Ahli Checker", page_icon=":tada:", layout="wide")

st.subheader("PKR Ahli Checker")
st.title("Welcome")

uploaded_file = st.file_uploader("Upload a CSV file", type = ["csv", "xlsx"])

if uploaded_file is not None:
    dataframe = pd.read_excel(uploaded_file)

    st.dataframe(dataframe)
    st.table(dataframe)