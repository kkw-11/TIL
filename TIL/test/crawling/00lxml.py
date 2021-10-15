import requests
from bs4 import BeautifulSoup
from lxml import etree
from urllib.request import urlopen


url = "https://pcmap.place.naver.com/restaurant/1368390925/menu/list"


response = urlopen(url)
htmlparser = etree.HTMLParser()
tree = etree.parse(response, htmlparser)
print(str(tree.xpath('//*[@id="app-root"]/div/div/div[2]/div[1]/div/div/div[2]')))