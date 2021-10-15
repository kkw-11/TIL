# 코알라유니브 스터디: 공공공공공경경 - 고주형
# 네이버 신지도 데이터 수집하기
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome("./chromedriver")
driver.get("https://map.naver.com/v5/search")

# 팝업 창 제거
driver.find_element_by_css_selector("button#intro_popup_close").click()

# 검색창에 검색어 입력하기
search_box = driver.find_element_by_css_selector("div.input_box>input.input_search")
search_box.send_keys("마라탕")

time.sleep(3)

# 검색버튼 누르기
search_box.send_keys(Keys.ENTER)

# 크롤링
for p in range(20):
    # 5초 delay
    time.sleep(2)
    
    js_script = "document.querySelector(\"body > app > layout > div > div.container > div.router-output > "\
                "shrinkable-layout > search-layout > search-list > search-list-contents > perfect-scrollbar\").innerHTML"
    raw = driver.execute_script("return " + js_script)

    html = BeautifulSoup(raw, "html.parser")

    contents = html.select("div > div.ps-content > div > div > div .item_search")
    for s in contents:
        search_box_html = s.select_one(".search_box")

        name = search_box_html.select_one(".title_box .search_title .search_title_text").text
        print("식당명: " + name)
        try:
            phone = search_box_html.select_one(".search_text_box .phone").text
        except:
            phone = "NULL"
        print("전화번호: " + phone)
        address = search_box_html.select_one(".ng-star-inserted .address").text
        print("주소: " + address)

        print("--"*30)
    # 다음 페이지로 이동
    try:
        next_btn = driver.find_element_by_css_selector("button.btn_next")
        next_btn.click()
    except:
        print("데이터 수집 완료")
        break

# 크롭 웹페이지를 닫음
driver.close()