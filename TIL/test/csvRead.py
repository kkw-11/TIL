import csv
import pandas
import chardet
import requests, json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def csv_read(src_file):
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument("window-size=1920x1080")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36")

    data = {}

    with open(src_file,"r", encoding='EUC-KR') as src:
        reader = csv.reader(src)

        for row in reader:
            url = f"https://map.naver.com/v5/search/{row[0]}"
            
            driver = webdriver.Chrome(options=options)
            driver.maximize_window()
            driver.get(url)

            #첫 Iframe 이동
            frame_elem = driver.find_element_by_id("searchIframe")
            driver.switch_to_frame(frame_elem)
            try:
                elem2 = driver.find_element_by_xpath('//*[@id="_pcmap_list_scroll_container"]/ul/li/div[1]/a/div[2]/span[1]') # searchIframe에 있는 별점 xpath
                data[row[0]] = elem2.text
                print("평점:",elem2.text)
                print(data)
                if row[0] == "이디야 시아테마파크점":
                    break
            except:
                try:
                    elem2 = driver.find_element_by_xpath('//*[@id="_pcmap_list_scroll_container"]/ul/li[1]/div[1]/a/div[2]/span[1]')
                    data[row[0]] = elem2.text
                    print("평점:",elem2.text)
                    if row[0] == "이디야 시아테마파크점":
                        break
                except:
                    continue
    return data

src_file = "crawling_data.csv"
data = csv_read(src_file)

print(data)

with open('./test.json', 'w', encoding='utf-8') as make_file:
    json.dump(data, make_file, indent="\t")