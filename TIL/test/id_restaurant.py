import csv
import pandas
import chardet
import requests, json
from requests.api import head
from requests.models import RequestEncodingMixin
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# detail_page = f"https://pcmap.place.naver.com/restaurant/{shop_id}/home?entry=bmp&from=map&fromPanelNum=2"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"}

url = "https://pcmap.place.naver.com/restaurant/1368390925/menu/list"

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36")
driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome()

driver.maximize_window()
# elem = driver.find_element_by_xpath('//*[@id="app-root"]/div/div/div[2]/div[4]/div/div[1]/div/ul/li[1]/a/div[2]/div[1]/div/span')
res = requests.get(url,headers=headers)

soup = BeautifulSoup(res,"html.parser")
elem = soup.find("div",attrs={"class":"place_section_content"})
print(elem.text)

