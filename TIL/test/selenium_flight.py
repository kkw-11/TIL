# 코알라유니브 스터디: 공공공공공경경 - 고주형
# 네이버 신지도 데이터 수집하기
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
frame_elem = driver.find_element_by_id("searchIframe")
driver.switch_to_frame(frame_elem)
# 팝업 창 제거
time.sleep(10)

print("hello")
# //*[@id="_pcmap_list_scroll_container"]/ul/li[1]/div[1]/a[1]/div[1]/div/span
# elem = driver.find_element_by_xpath('//*[@id="_pcmap_list_scroll_container"]/ul/li[1]/div[1]/a[1]/div[1]/div/span').click()
# try:
elem = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/div[1]/a[1]/div[2]/div')

print(elem.text)
elem.click()
time.sleep(5)

frame_elem = driver.find_element_by_id("entryIframe")

driver.switch_to_frame(frame_elem)

# elem = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="_pcmap_list_scroll_container"]/ul/li[1]/div[1]/a[1]/div[1]/div')))
elem = driver.find_element_by_xpath('//*[@id="app-root"]/div/div/div[2]/div[1]/div/div/div[1]/div/span[1]/em')
print(elem.text)

# except:
print("fail")

# 검색버튼 누르기
# search_box.send_keys(Keys.ENTER)

# # 검색버튼 누르기
# search_box.send_keys(Keys.ENTER)
# elem = browser.find_element_by_name("search_query")
# elem.click()
# elem.send_keys("아웃백")
# elem.send_keys(Keys.ENTER)
# elem = browser.find_element_by_xpath("//*[@id='ct']/div[2]/ul/li[1]/div[1]/a[2]/div/strong")
# elem.click()
