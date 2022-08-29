from urllib import response
from urllib.request import Request, urlopen
import json
import pandas as pd
from openpyxl import load_workbook

url = 'https://api.keadilanrakyat.org/member/findByIC/'
file_location = "Book (1).xlsx"
dataframe = pd.read_excel(file_location)
ExcelWorkbook = load_workbook(file_location)
ada_ke_tak = []

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
    except:
        ada_ke_tak.append("No")

dataframe["daftar_or_nah"] = ada_ke_tak
dataframe.to_excel(file_location, index = False)