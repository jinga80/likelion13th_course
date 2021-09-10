from selenium import webdriver
from bs4 import BeautifulSoup

import time

url = 'https://pythonstart.github.io/web/'
start = time.time()
driver = webdriver.Chrome('/opt/homebrew/bin/chromedriver')
driver.get(url)