from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

_input = input("가게명을 입력하세요:")

url = f"https://map.naver.com/v5/search/{_input}"
driver = webdriver.Chrome("./chromedriver")
driver.get(url)