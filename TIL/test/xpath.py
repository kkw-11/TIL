import requests, json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

_input = input("검색어 입력")
# https://pcmap.place.naver.com/restaurant/{}
url = f"https://map.naver.com/v5/search/{_input}"
driver = webdriver.Chrome("./chromedriver")
driver.get(url)

#첫 Iframe 이동
frame_elem = driver.find_element_by_id("searchIframe")
driver.switch_to_frame(frame_elem)

elem = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/div[1]/a[1]/div[2]/div') #검색된 첫 번째 가게이름 xpath, 클릭해서 새로운 창 띄우기 위한 용도

# print(elem.text)
#별점
elem2 = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/div[1]/a[2]/div/span[1]/em') # searchIframe에 있는 별점 xpath
print("평점:",elem2.text)

time.sleep(10)
elem.click()
driver.switch_to_frame('entryIframe')

time.sleep(5) # 

elem = driver.find_element_by_xpath('//*[@id="app-root"]/div/div/div[2]/div[4]/div/div[3]/div/ul/li[2]/div/a/span[1]') #가게이름 클릭후 우측에 새로 뜨는 창에서 주소 xpath
print(elem.text)

