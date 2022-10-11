from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome(executable_path="/Users/park-yeojun/Dev/Resource/chromedriver")
browser.get('https://python.org')

menus = browser.find_elements(By.CSS_SELECTOR,  '#top ul.menu li')
 
pypi = None
for m in menus:
    if m.text == "PyPI":
        pypi = m
    print(m.text)
 
pypi.click()  # 클릭
 
time.sleep(5) # 5초 대기
browser.quit() # 브라우저 종료

