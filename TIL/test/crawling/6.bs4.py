import requests
from bs4 import BeautifulSoup

url = "https://webtoonscorp.com/"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
print(soup.title)
print(soup.title.get_text())
print(soup.a.attrs)
print(soup.a["href"])

print(soup.find("a", attrs={"class":"sb_ico"}))