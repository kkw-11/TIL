import requests, json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

_input = input("검색어 입력")
url = f"https://m.map.naver.com/search2/search.naver?query={_input}"
res = requests.get(url)

soup = BeautifulSoup(res.text,"html.parser")
print(soup)
import re
shop_ids = re.findall(r's(\d*)', str(soup))

# 가게들의 id가 중복되어 많이 검색되므로 set로 변환
shop_ids = set(shop_ids)
print(len(shop_ids))





