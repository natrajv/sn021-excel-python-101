#*==Excel-101==*
#*--Objective:-
#* 1. Create, Open, Read, Write, and Modify Excel files using Python.
#*--Pre-requisites:-
#* 1. IDE: VSCode, Jupyter Lab, Git, 
#* 2. Tools: Python 3.13, UV
#* 3. Libraries: openpyxl, pandas, numpy, xlrd, xlsxwriter
#*--Config:-
#* 1. Home directory: d:\ws\sn021
#*--Source:-
#* ChatGPT link: 
#*=====*
#*==Index-Codes==*
#@Code-01: Open, Read/Update Cell & Save
#@Code-02: 

#*==Details-Codes==*
#@Code-01: Create, Open, Read/Update Cell & Save
#*--Step-1: Create, Read & Save
'''#Skip @Step-1
import openpyxl
from openpyxl import workbook
wb = workbook.Workbook()
ws = wb.active
ws['A1'] = 42
ws.append([1, 2, 3])
wb.save("test.xlsx")
'''
#*--Step-2: Open, Read to DataFrame, Close
import pandas as pd
df = pd.read_excel(r'db\jee-mains.xlsx')
#--DataFrame Instpection
print("DataFrame Inspection:")
print("---------------------")
print("\nDataFrame Shape:")
print(df.shape)
print("\nDataFrame Columns:")
print(df.columns)
print("First 5 Rows:")
print(df.head())
print("\nLast 5 Rows:")
print(df.tail())
print("\nDataFrame Info:")
print(df.info())
print("\nDataFrame Description:")
print(df.describe())
 
#*---Outcome

#*---Note

#*-----*
#@Step-2: ...
 
#*---Outcome

#*---Note

#*-----*

#**==Issues Note==**
#>> 1. Invalid escape sequence '\j' in Excel file path.
#*--Root Cause
#> Using a single backslash in file paths can create invalid escape sequences in Python strings.
#*--Resolution
#> Use raw strings (prefix the string with 'r') or double backslashes to define file paths.
#> Example: r'db\jee-mains.xlsx' or 'db\\jee-mains.xlsx'
#*--Note
#> ...
#> Gemini link: https://tinyurl.com/sn021-01
#*-----*
#>> 2. <...>
#*--Root Cause
#> ...
#*--Resolution
#> ...
#*--Note
#> ...
#> ChatGPT link: ...
#*-----*
#>> 2. <...>
#*--Root Cause
#> ...
#*--Resolution
#> ...
#*--Note
#> ...
#> ChatGPT link: ...
#*-----*

#**==References==**
#[01] ...

#**==Version==**
# Version: 1.0.0
# Tag: SN021-V1.0.0
#* CTD: 20250930_1250
#* LUD: 20251016_0835
#**=====**
