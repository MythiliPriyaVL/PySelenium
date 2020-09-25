import openpyxl
from openpyxl import Workbook

excel_file = openpyxl.load_workbook('Holidays.xlsx')
excel_sheet = excel_file['Holidays_2019']

# delete column
excel_sheet.delete_cols(idx=2)  # B=2

# delete row
excel_sheet.delete_rows(idx=2, amount=2)  # rows 2,3 are deleted

excel_file.save('Holidays.xlsx')