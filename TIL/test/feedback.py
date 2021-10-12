import requests, json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

_input = input("검색어 입력")
url = f"https://map.naver.com/v5/search/{_input}"
driver = webdriver.Chrome("./chromedriver")
driver.get(url)

# 여기서 각 가게들의 id를 다음과 같이 추출합니다.
import re
shop_ids = re.findall(r'PlaceSummary:(\d*)', driver.page_source)


# 가게들의 id가 중복되어 많이 검색되므로 set로 변환
shop_ids = set(shop_ids)
print(len(shop_ids))

# 저의 경우 44개로 출력확인.
# 가게 클릭했을때 상세페이지 URL은 다음과 같이 확인
# https://pcmap.place.naver.com/restaurant/%7Bshop_id%7D/home?entry=bmp&from=map&fromPanelNum=2

# 따라서 상세페이지는 아래와 같이 들어가면 됨.
for shop_id in shop_ids:
    detail_page = f"https://pcmap.place.naver.com/restaurant/{shop_id}/home?entry=bmp&from=map&fromPanelNum=2"
    driver.get(detail_page)
    #이후 상세페이지 크롤링 작업하시면 됩니다. 
    #...
    time.sleep(5)