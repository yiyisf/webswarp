"""
提取国家代码
"""
import requests
from bs4 import BeautifulSoup
import MySQLdb

BASE_URL = 'http://www.hscode.net/IntegrateQueries/QueryPageGB'


def get_data(index, cur):
    rs = requests.post(BASE_URL, {'pageIndex': index, 'taxKey': ''})
    # print(rs.text)
    bs = BeautifulSoup(rs.text, "html5lib")
    names = bs.find_all('span', class_="tcon")
    i = int(len(names)/3)
    # print(i)

    for ii in range(i):
        # print('code:',names[ii*2].string.strip())
        # print('name:',names[ii*2 + 1].string.strip())
        code = names[ii*3].string.strip()
        name_cn = names[ii*3 + 1].string.strip()
        # name_en = names[ii*3 + 2].string.replace("'","\\")
        if names[ii*3 +2].string == None:
            print(code)
            name_en = ''
        else:
            name_en = names[ii * 3 + 2].string.replace("'", "\\")

        sql = "INSERT INTO countries (code, name_cn, name_en) VALUES ('%s', '%s', '%s')" % (code, name_cn, name_en)

        try:
            cur.execute(sql)
        except:
            db.rollback()
            print('rollback')
            print(sql)


db = MySQLdb.connect(host='127.0.0.1', port=3307, user='root', passwd='111111', db='customs', charset='utf8')
cursor = db.cursor()


if __name__ == '__main__':
    # get_data(4, None)
    for i in range(17):
        get_data(i+1, cursor)
        db.commit()
        print('已完成第%s页' % str(i+1))

    cursor.close()


