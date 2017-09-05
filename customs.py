import requests
from bs4 import BeautifulSoup
import re
import MySQLdb

"""
提取报关要素
"""
BASE_URL = "http://www.hscode.net/IntegrateQueries/YsInfoPager"


def get_data(index, cur):
    rs = requests.post(BASE_URL, {"pageIndex": index})
    # re.encoding('utf-8')
    html = rs.text

    bs = BeautifulSoup(html, "html5lib")

    items = bs.find_all('div', class_='scx_item')

    # sql = "INSERT INTO declear_ele_cn(code, \
    #    name, items, unit1, unit2, rate_best, rate_in, rate_temp_in, rate_sale, rate_out, rate_back, vat, regular_cond, quarantine_type, dict) \
    #    VALUES ('%d', '%s', '%s', '%s', '%s' , '%s', '%s', '%s', '%s' , '%s', '%s', '%s', '%s', '%s', '%s' )" % \
    #    ('Mac', 'Mohan', 20, 'M', 2000)
    # code = 0
    # name, items, unit1, unit2, rate_best, rate_in, rate_temp_in, rate_sale, rate_out, rate_back, vat, regular_cond, quarantine_type, dict = ''
    for item in items:
        # print('===========================================================')

        # print("商品编码：", item.find('div', class_='even red').string)
        code = item.find('div', class_='even red').string.strip()
        # 原处理方法
        ts = item.find_all('table')
        # 打印测试
        # for t in ts:
        #     print(t.find('div', class_='odd').string, t.span.string)

        name = ts[0].span.string.strip()
        items = ts[1].span.string.strip()
        dict = ts[2].span.string.strip()

        # evens = item.find_all('div', class_='row_0')
        # for even in evens:
        #     # print(even.find(class_='odd').string, even.find(attrs={'class' : re.compile('even')}).string)
        #
        #     if len(even.find_all(class_='odd')) == 1:
        #         print(even.find(class_='odd').string, even.find(attrs={'class' : re.compile('even')}).string)
        #     else :
        #         odds = even.find_all(class_='odd')
        #         names = even.find_all(attrs={'class' : re.compile('even')})
        #         for i in range(len(even.find_all(class_='odd'))):
        #             print(odds[i].string, names[i].string, sep=":")

        even1s = item.find_all('div', class_='even1')

        unit1 = even1s[0].string.strip()
        unit2 = even1s[1].string.strip()
        rate_best = even1s[2].string.strip()
        rate_in = even1s[3].string.strip()
        rate_temp_in = even1s[4].string.strip()
        rate_sale = even1s[5].string.strip()
        rate_out = even1s[6].string.strip()
        rate_back = even1s[7].string.strip()
        vat = even1s[8].string.strip()
        regular_cond = even1s[9].label.string.strip()
        quarantine_type = even1s[10].label.string.strip()

        # print(regular_cond)

        sql = "INSERT INTO declear_ele_cn(code, name, items, unit1, unit2, rate_best, rate_in, rate_temp_in, rate_sale, rate_out, rate_back, vat, regular_cond, quarantine_type, dict) VALUES ('%s', '%s', '%s', '%s', '%s' , '%s', '%s', '%s', '%s' , '%s', '%s', '%s', '%s', '%s', '%s' )" % (code, name, items, unit1, unit2, rate_best, rate_in, rate_temp_in, rate_sale, rate_out, rate_back, vat, regular_cond, quarantine_type, dict)
        # cur.execute(sql)
        try:
            cur.execute(sql)
        except:
            db.rollback()
            print('rollback')


# db = MySQLdb.connect('127.0.0.1', 'root', '111111', 'customs')
db = MySQLdb.connect(host='127.0.0.1', port=3307, user='root', passwd='111111', db='customs', charset='utf8')
cursor = db.cursor()

# for i in range(2364):
    # get_data(i+1, cursor)

if __name__ == '__main__':
    # pass
    # get_data(1, cursor)
    # db.commit()
    for i in range(170, 2364):
        get_data(i+1, cursor)
        db.commit()
        print('已完成第%s页' % str(i+1))

