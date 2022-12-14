from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup

options = Options()
options.add_argument("--disable-notifications")

chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
chrome.get("https://www.facebook.com/")

email = chrome.find_element("id","email")
password = chrome.find_element("id","pass")

email.send_keys('a0224658939@yahoo.com.tw')
password.send_keys('*****')
password.submit()

time.sleep(3)
chrome.get('https://www.facebook.com/learncodewithmike')

# 執行滾動捲軸
for x in range(1, 4):
    chrome.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(5)

soup = BeautifulSoup(chrome.page_source, 'html.parser')

titles = soup.find_all('span', {
    'class': 'a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7 ojkyduve'})

for title in titles:

    post = title.find('span', {'dir': 'auto'})

    if post:
        print(post.getText())

chrome.quit()