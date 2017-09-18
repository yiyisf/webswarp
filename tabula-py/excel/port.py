import xlrd


f = xlrd.open_workbook('port Codes.xls')

for s in f.sheets():
    print(s.nrows)