# 코알라유니브 스터디: 공공공공공경경 - 고주형
# 네이버 신지도 데이터 수집하기
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup


key_word = input("키워드를 입력하세요 :")

browser = webdriver.Chrome("./chromedriver.exe")
time.sleep(3)

browser.get("https://naver.com")
time.sleep(3)

# #로그인 버튼 찾기
# elem = browser.find_element_by_class_name("link_login")
# time.sleep(3)
# #로그인 버튼 클릭
# elem.click()
# time.sleep(3)
# #뒤로가기
# browser.back()
# time.sleep(3)
# #앞으로 가기
# browser.forward()
# time.sleep(3)

# time.sleep(3)
# browser.back()

elem = browser.find_element_by_id('query')
elem.send_keys(key_word)
elem = browser.find_element_by_xpath("//*[@id='search_btn']/span[2]")
elem.click()
# elem.send_keys(Keys.ENTER)
elem = browser.find_elements_by_tag_name("a")
for e in elem:
    t = e.get_attribute("href")
    print(t)
browser.quit()