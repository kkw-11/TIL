import requests
from bs4 import BeautifulSoup
from lxml import etree

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

_input = input("가게명 입력: ")

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"}
url = "https://m.map.naver.com/search2/search.naver?query="

driver = webdriver.Chrome("./chromedriver")

driver.get(url)
elem = driver.find_element_by_tag_name("li")

print(elem)