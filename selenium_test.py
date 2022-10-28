import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

driver = Chrome("./chromedriver")
# ".":這一層   "..":上一層
driver.get("https://www.google.com")
driver.maximize_window()
# 將頁面放大maximize_window()
# print(driver.page_source)
# find. find_all -> find_element, find_elements
e = driver.find_element_by_class_name("gLFyf")
# send_keys輸入
e.send_keys("天竺鼠車車")
e.send_keys(Keys.ENTER)
while True:
    time.sleep(1)
    # 模擬等待時間
    es = driver.find_elements_by_class_name("yuRUbf")
    for e in es:
        link = e.find_element_by_tag_name("a")
        # .text["href"] -> .text   .get_attribute("href")
        print(link.text)
        print(link.get_attribute("href"))
        print("-" * 30)
    try:
        e = driver.find_element_by_id("pnnext")
        e.click()
    except NoSuchElementException:
        break
time.sleep(3)
driver.close()