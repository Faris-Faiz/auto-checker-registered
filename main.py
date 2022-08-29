import streamlit as st
import pandas as pd
import json
from urllib.request import Request, urlopen
from openpyxl import load_workbook

st.set_page_config(page_title="PKR Ahli Checker", page_icon=":tada:", layout="wide")

st.subheader("PKR Ahli Checker")
st.title("Welcome")

uploaded_file = st.file_uploader("Upload a CSV file", type = ["csv", "xlsx"])

if uploaded_file is not None:
    dataframe = pd.read_excel(uploaded_file)

    st.dataframe(dataframe)

result = st.button("Check if they are a PKR member")
if (result):
    url = 'https://api.keadilanrakyat.org/member/findByIC/'
    dataframe = pd.read_excel(uploaded_file)
    ExcelWorkbook = load_workbook(uploaded_file)
    ada_ke_tak = []
    ic_list_takRegister = []
    ic_list_Register = []

    for i in range(len(dataframe)):
        url_ic = url
        ic_number = dataframe.iloc[i, 1]
        ic_number_noSpace = ic_number.replace(' ', '')
        url_ic += ic_number_noSpace

        req = Request(url_ic, headers={'User-Agent': 'Mozilla/5.0'})
        
        try:
            webpage = urlopen(req)
            data = json.loads(webpage.read())
            ada_ke_tak.append("Yes")
            ic_list_Register.append(dataframe.iloc[i, 1])
        except:
            ada_ke_tak.append("No")
            ic_list_takRegister.append(dataframe.iloc[i, 1])

    dataframe["daftar_or_nah"] = ada_ke_tak
    dataframe.to_excel(uploaded_file, index = False)
    st.dataframe(dataframe)

    st.write("Yang ni registered as PKR members")
    st.dataframe(ic_list_Register)

    st.write("Yang ni tak registered as PKR members")
    st.dataframe(ic_list_takRegister)