import requests
from bs4 import BeautifulSoup
import re
import MySQLdb


BASE_URL = "http://www.hscode.net/IntegrateQueries/YsInfoPager"


rs = requests.post(BASE_URL, {"pageIndex": 2})
# re.encoding('utf-8')
html = rs.text

bs = BeautifulSoup(html, "html5lib")

items = bs.find_all('div', class_='scx_item')


def get_data(index):
    # sql = "INSERT INTO declear_ele_cn(code, \
    #    name, items, unit1, unit2, rate_best, rate_in, rate_temp_in, rate_sale, rate_out, rate_back, vat, regular_cond, quarantine_type, dict) \
    #    VALUES ('%d', '%s', '%s', '%s', '%s' , '%s', '%s', '%s', '%s' , '%s', '%s', '%s', '%s', '%s', '%s' )" % \
    #    ('Mac', 'Mohan', 20, 'M', 2000)
    code = 0
    # name, items, unit1, unit2, rate_best, rate_in, rate_temp_in, rate_sale, rate_out, rate_back, vat, regular_cond, quarantine_type, dict = ''
    for item in items:
        # print('===========================================================')

        # print("商品编码：", item.find('div', class_='even red').string)
        cod = item.find('div', class_='even red').string
        # 原处理方法
        ts = item.find_all('table')
        for t in ts:
            print(t.find('div', class_='odd').string, t.span.string)

        evens = item.find_all('div', class_='row_0')
        for even in evens:
            # print(even.find(class_='odd').string, even.find(attrs={'class' : re.compile('even')}).string)

            if len(even.find_all(class_='odd')) == 1:
                print(even.find(class_='odd').string, even.find(attrs={'class' : re.compile('even')}).string)
            else :
                odds = even.find_all(class_='odd')
                names = even.find_all(attrs={'class' : re.compile('even')})
                for i in range(len(even.find_all(class_='odd'))):
                    print(odds[i].string, names[i].string, sep=":")





# db = MySQLdb.connect('127.0.0.1', 'root', '111111', 'customs')
# cursor = db.cursor()



# for i in range(2364):
    # get_data(i+1, cursor)

if __name__ == '__main__':
    get_data(1)

