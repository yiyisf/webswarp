import MySQLdb
from tabula import read_pdf

# create db connect
# db = MySQLdb.connect(host='192.168.1.252', port=3305, user='root', passwd='slysSE4RFV', db='ecus', charset='utf8')
db = MySQLdb.connect(host='127.0.0.1', port=3307, user='root', passwd='111111', db='customs', charset='utf8')
cursor = db.cursor()
# read pdf file and convert table to json
js = read_pdf("pdf/modeoftransport.pdf", output_format="json")
print("-=-=-=-=-=STARTING-=-=-=-=")
# get the table data
item = js[0]['data']

for i in range(1, len(item)):
    # print(item[i][0]['text'], item[i][1]['text'], sep=":")
    code = item[i][0]['text']
    name = item[i][1]['text']
    sql = "INSERT INTO transport_mode(code, name) VALUES ('%s', '%s')" % (
    code, name)
    try:
        cursor.execute(sql)
    except:
        db.rollback()
        print('rollback')
    print("complate: %s" % str(i/(len(item) -1)*100).split('.')[0], "%")


db.commit()
