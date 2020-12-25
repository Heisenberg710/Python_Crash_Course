from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/pages/warandpeace.html")
# 定义解释器
bsObj = BeautifulSoup(html, 'html.parser')

nameList = bsObj.findAll("span", {"class": "green"})
for name in nameList:
    print(name)