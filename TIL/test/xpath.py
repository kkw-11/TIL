# 코알라유니브 스터디: 공공공공공경경 - 고주형
# 네이버 신지도 데이터 수집하기
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

#첫 Iframe 이동
frame_elem = driver.find_element_by_id("searchIframe")
driver.switch_to_frame(frame_elem)

time.sleep(10)

print("hello")
elem = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/div[1]/a[1]/div[2]/div')

# print(elem.text)
#별점
elem2 = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/div[1]/a[2]/div/span[1]/em')
print(elem2.text)
elem3 = driver.find_element_by_xpath('//*[@id="baseMap"]/div[1]/div/div[1]/div[3]/div[2]/div[1]/salt-marker/div/button')

elem.click()

time.sleep(5)
print(elem3)
req = requests.get(url)
print(req.status_code)
soup = BeautifulSoup(req.text, "html.parser")

elem2 = driver.find_element_by_class_name('__WebInspectorHideElement__')
print(elem2.text)

elem = driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[1]/div/div/div[1]/div/span[1]/em')
print(elem.text)

# frame_elem = driver.find_element_by_id("entryIframe")

# driver.switch_to_frame(frame_elem)
# elem = driver.find_element_by_xpath('//*[@id="app-root"]/div/div/div[2]/div[1]/div/div/div[1]/div/span[1]/em')

# elem2 = driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[1]/div/div/div[1]/div/span[1]')

# print(elem.text)
# print(elem2.text)

