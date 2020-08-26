import pandas as pd

excelfile = pd.ExcelFile('input File.xlsx')
dframe =excelfile.parse('Top 10 Europe')
print(dframe)

