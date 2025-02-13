from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time

service = Service(r'/chromedriver')
driver = webdriver.Chrome(service=service)

driver.get('https://google.pl')

search_box = driver.find_element(By.NAME, 'q')

search_box.send_keys('selenium python')

search_box.submit()

time.sleep(5)

driver.quit()