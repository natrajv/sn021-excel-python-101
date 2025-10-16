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


#*--Step-2: Open, Read/Update Cell & Save
#xl = workbook.load_workbook("test.xlsx")
 
#*---Outcome

#*---Note

#*-----*
#@Step-2: ...
 
#*---Outcome

#*---Note

#*-----*

#**==Issues Note==**
#>> 1. ...
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
# Tag: sn021-v1.0.0
#* CTD: 20250930_1250
#* LUD: 20251016_0835
#**=====**
