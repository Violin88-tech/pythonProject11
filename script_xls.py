from xlrd import open_workbook
workbook = open_workbook("tmp/Книга_5.xls")
print(workbook.nsheets)

