import requests
from bs4 import BeautifulSoup


a = requests.get('https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/')
html = a.content

bs = BeautifulSoup(html)
print(bs.prettify())