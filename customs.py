import requests
from bs4 import BeautifulSoup


BASE_URL = "http://www.hscode.net/IntegrateQueries/YsInfoPager"

re = requests.post(BASE_URL,{"pageIndex": 2})
# re.encoding('utf-8')
html = re.text

bs = BeautifulSoup(html, "html5lib")

items = bs.find_all('div', class_='scx_item')


for item in items:
    print('===========================================================')
    print("商品编码：", item.find('div', class_='even red').string)
    # print('商品名称:', item.find_next('table').find('span').string)
    # print('申报要素:', item.find_next('table').find('span').string)
    ts = item.find_all('table')
    for t in ts:
        print(t.span.string)

    evens = item.find_all('div', class_='even1')
    for even in evens:
        print(even.string)
