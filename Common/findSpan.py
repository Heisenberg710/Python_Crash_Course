from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://k.sina.cn/article_7032866777_1a33107d900100kjd2.html")
# 定义解释器
bsObj = BeautifulSoup(html, 'html.parser')

nameList = bsObj.findAll("p")
for name in nameList:
    print(name)