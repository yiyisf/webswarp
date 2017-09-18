import MySQLdb
import xlrd


db = MySQLdb.connect(host='127.0.0.1', port=3307, user='root', passwd='111111', db='customs', charset='utf8')
cursor = db.cursor()
# data = xlrd.open_workbook('Package Type.xlsx')
data = xlrd.open_workbook('Two Digit Country Codes.xlsx')

sheets = data.sheets()
table1 = sheets[0]

print(table1.nrows)

len = table1.nrows

for i in range(1, len):
    code = table1.row(i)[0].value
    name = table1.row(i)[1].value

    sql = 'INSERT INTO asycuda_country(code, name) VALUES ("%s", "%s")' % (
    code, name)
    try:
        cursor.execute(sql)
    except:
        # db.rollback()
        print('rollback: %s' % sql)
    print("complate %s : %s" % (code, str(i/(len -1)*100).split('.')[0]), "%")


db.commit()


