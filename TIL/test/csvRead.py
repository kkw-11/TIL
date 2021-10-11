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

    books = []

    with open(src_file,"r", encoding='EUC-KR') as src:
        reader = csv.reader(src)

        for row in reader:
            _input = row[4]
            print(_input)
            url = f"https://map.naver.com/v5/search/{_input}"
            driver = webdriver.Chrome("./chromedriver")
            driver.get(url)

            #첫 Iframe 이동
            frame_elem = driver.find_element_by_id("searchIframe")
            driver.switch_to_frame(frame_elem)
            elem = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/div[1]/a[1]/div[2]/div')

            # print(elem.text)
            #별점
            elem2 = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/div[1]/a[2]/div/span[1]/em')
            print(elem2.text)
            elem3 = driver.find_element_by_xpath('//*[@id="baseMap"]/div[1]/div/div[1]/div[3]/div[2]/div[1]/salt-marker/div/button')

            elem.click()


src_file = 'team.csv'
csv_read(src_file)
