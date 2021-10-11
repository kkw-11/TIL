from selenium import webdriver
driver = webdriver.Chrome("./chromedriver")
# 구버전 네이버지도 접속
driver.get("https://v4.map.naver.com")

driver.find_elements_by_css_selector("button.btn_close")[1].click()

# 검색창에 검색어 입력하기 // 검색창: input#search-input
search_box = driver.find_element_by_css_selector("input#search-input")
search_box.send_keys("치킨")
# 검색버튼 누르기 // 검색버튼: button.spm
search_button = driver.find_element_by_css_selector("button.spm")
search_button.click()