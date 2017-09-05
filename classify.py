"""
提取归类决定
"""
import requests
from bs4 import BeautifulSoup
import MySQLdb

BASE_URL = 'http://www.hscode.net/IntegrateQueries/QueryJD/%d?q1=&q2=&q3=&q4='


def get_data(index, cur):
    pass
    # i = 3
    rs = requests.post(BASE_URL % index, {'isAjax': 1})
    bs = BeautifulSoup(rs.text, "html5lib")
    items = bs.find_all('div', class_='scx_item')
    for item in items:
        ss = item.find_all('div', class_='even1 red')
        code = ss[0].string.strip()
        if len(ss) > 1:
            status = ss[1].string.strip()
        else:
            status = item.find('div', class_='even1 blue').string.strip()

        # code = item.find('div', class_='even1 red').string.strip()
        # status = item.find('div', class_='even1 blue').string.strip()

        evens = item.find_all('div', class_='even')
        name_cn = evens[0].string.strip()
        name_en = evens[1].string.strip()
        name_oth = evens[2].string.strip()
        rate_role_num = evens[3].string.strip()
        customs_post = evens[4].string.strip()

        even1s = item.find_all('div', class_='even1')
        start_date = even1s[2].string.strip()
        pub_date = even1s[3].string.strip()

        sql = "INSERT INTO classify_role (code, status, name_cn, name_en, name_oth, rate_role_num, customs_post, start_date, pub_date) VALUES ('%s', '%s', '%s', '%s', '%s' , '%s', '%s', '%s', '%s' )" % (
        code, status, name_cn, name_en, name_oth, rate_role_num, customs_post, start_date, pub_date)

        # print(sql)

        try:
            cur.execute(sql)
        except:
            db.rollback()
            print('rollback')

        # print('编号:', code)
        # print('状态:', status)
        # print('名称:', name_cn)
        # print('日期:', start_date)

        # good = requests.get('http://www.hscode.net/IntegrateQueries/QueryJDDetail/?guid=%s'%code)
        # googbs = BeautifulSoup(good.text.strip('"'), "html5lib")
        # print(googbs.text)
        # s = googbs.find_all('li')
        # print(s)
        # print(s[0].span.string)

db = MySQLdb.connect(host='127.0.0.1', port=3307, user='root', passwd='111111', db='customs', charset='utf8')
cursor = db.cursor()

# for i in range(2364):
    # get_data(i+1, cursor)




if __name__ == '__main__':
    # pass
    # get_data(1, cursor)
    # db.commit()
    for i in range(544):
        get_data(i+1, cursor)
        db.commit()
        print('已完成第%s页' % str(i+1))

    cursor.close()


