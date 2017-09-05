"""
提取关区代码/贸易方式
"""
import requests
from bs4 import BeautifulSoup
import MySQLdb

# BASE_URL = 'http://www.hscode.net/IntegrateQueries/QueryPageGQ'      #关区代码
BASE_URL = 'http://www.hscode.net/IntegrateQueries/QueryPageMY'  #贸易方式


def get_data(index, cur):
    rs = requests.post(BASE_URL, {'pageIndex': index, 'taxKey': ''})
    # print(rs.text)
    bs = BeautifulSoup(rs.text, "html5lib")
    codes = bs.find_all('span', class_="tcon fontnumber")
    names = bs.find_all('span', class_="tcon")

    # print(len(codes))
    # print(len(names))

    i = int(len(names)/3)   #for 关区
    # i = int(len(names)/2)  #for 贸易方式
    # print(i)

    for ii in range(i):
        # print('code:',names[ii*2].string.strip())
        # print('name:',names[ii*2 + 1].string.strip())

        # sql = "INSERT INTO customs_area (code, name) VALUES ('%s', '%s')" % (names[ii*2].string.strip(), names[ii*2 + 1].string.strip())
        sql = "INSERT INTO bussness_type (code, name, dict) VALUES ('%s', '%s', '%s')" % (names[ii*3].string.strip(), names[ii*3 + 1].string.strip(), names[ii*3 + 2].string.strip())

        # print(sql)

        try:
            cur.execute(sql)
        except:
            db.rollback()
            print('rollback')



    # for item in items:
    #     ss = item.find_all('div', class_='even1 red')
    #     code = ss[0].string.strip()
    #     evens = item.find_all('div', class_='even')
    #     name = evens[0].string.strip()
    #


db = MySQLdb.connect(host='127.0.0.1', port=3307, user='root', passwd='111111', db='customs', charset='utf8')
cursor = db.cursor()


if __name__ == '__main__':
    # get_data(1, None)
    for i in range(7):
        get_data(i+1, cursor)
        db.commit()
        print('已完成第%s页' % str(i+1))

    cursor.close()


