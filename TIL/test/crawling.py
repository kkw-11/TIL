import urllib.request 
import requests, json
from bs4 import BeautifulSoup
from requests.api import request
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# request라이브러리에서 헤더 사용

driver = webdriver.Chrome('./chromedrive')
driver.implicitly_wait(3)

def open_api():
    url = "http://openapi.foodsafetykorea.go.kr/api/929d4adad1ec4857a263/C004/json/1/2"
    req = requests.get(url)

    if req.status_code == requests.codes.ok:
        print("connection success!")
        print(req.text)
    else:
        print("connection fail!")

    # json_str = response.read().decode("utf-8")
    # json_object = json.loads(json_str)

    # print(data)

# # def find_restaurant():
# #     # a = []
# #     # p = "유황오리진흙구이관악구청지점 서울특별시 송파구 새말로"

# #     # url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q="
# #     # url = url + p
# #     # req = requests.get(url)
# #     # soup = BeautifulSoup(req.text,"html.parser")
# #     # ul_tag = soup.find("div", class_="inner_article").find("ul",class_="list_place")
# #     # if ul_tag != None:
# #     #     find_tag = a.append( ul_tag.find("div", class_="wrap_cont").find("a").text) 


# #     # print(a)

# #     # print("지역과 메뉴명을 입력하세요")

# #     place = ["이촌동 면옥 ", "이층손만두", "이코노스시", "이탈리안갈릭(대학로본점)", "이태리식당라-스텔라", "이태원가든", "이태원써브웨이"	, "이태원천상동여의도점", "이태원천상여의도점	"	,"	이푸드	"	,"	이필배의 진짜루명태촌	"	,"	이학갈비	"	,"	이학면옥	"	,"	이한 불판	"	]    
    
# #     for p in place:
# #         url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q="
# #         url = url+p

# #         req = requests.get(url)

# #         print(req.status_code)
# #         # print(req.text)
# #         soup = BeautifulSoup(req.text,"html.parser")
# #         ul_tag = soup.find("div", class_="inner_article").find("ul",class_="list_place")
# #         no = []
# #         if ul_tag != None:
# #             find_tag = ul_tag.find_all("li")
# #         else:
# #             no.append(p)
# #             print("no")
         
# #         a= []
# #         for d in find_tag:
# #             a.append( d.find("div", class_="wrap_cont").find("a").text) 

# #         print(a)
# #         print(no)

def find_address():
    url = "https://map.naver.com/v5/search/흑다우"
    # place = "흑다우"
    # url = url + place

    req = requests.get(url)
    print(req.status_code)
    soup = BeautifulSoup(req.text, "html.parser")
    time.sleep(5)
    div_tag = soup.find("body",attrs={"class":"place_on_pcmap"})
    print(div_tag)

    # print(div_tag.find("a").text)

if __name__ == "__main__" :
    # find_restaurant()
    find_address()
    # open_api()
