import requests
from bs4 import BeautifulSoup
from lxml import etree


url = "https://pcmap.place.naver.com/restaurant/1368390925/menu/list"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
print(soup.title)
print(soup.title.get_text())
print(soup.a.attrs)
print(soup.a["href"])

print(soup.find("a", attrs={"class":"sb_ico"}))

print(soup.find('/html/body/div[3]/div/div/div[2]/div[1]/div/div/div[2]'))