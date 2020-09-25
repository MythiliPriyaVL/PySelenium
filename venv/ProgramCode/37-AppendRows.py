import openpyxl
from openpyxl import Workbook

excel_file = openpyxl.load_workbook('Holidays.xlsx')
excel_sheet = excel_file['Holidays_2019']

holiday_rows = (
    ('Black Friday', 'Fourth Thursday of November, Shopping Day', '11/29/19'),
    ('Holi', 'Festival of Colors', '3/20/19')
)

for row in holiday_rows:
    excel_sheet.append(row)

excel_file.save('Holidays.xlsx')