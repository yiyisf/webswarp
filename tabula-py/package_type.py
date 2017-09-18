from tabula import read_pdf
import MySQLdb


db = MySQLdb.connect(host='127.0.0.1', port=3307, user='root', passwd='111111', db='customs', charset='utf8')
cursor = db.cursor()

pdf = read_pdf("pdf/termofdelivery.pdf", output_format="json")
# print(pdf)
item = pdf[0]['data']

for i in range(1, len(item)):
    # print(item[i][0]['text'], item[i][1]['text'], sep=":")
    code = item[i][0]['text']
    name = item[i][1]['text']
    sql = "INSERT INTO delivery_mode(code, name) VALUES ('%s', '%s')" % (
    code, name)
    try:
        cursor.execute(sql)
    except:
        db.rollback()
        print('rollback')
    print("complate: %s" % str(i/(len(item) -1)*100).split('.')[0], "%")


db.commit()
