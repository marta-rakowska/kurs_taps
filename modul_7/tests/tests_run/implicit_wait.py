from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://simpletestsite.fabrykatestow.pl/')
myDynamicElement = driver.find_element(By.ID, 'checkbox-header')
driver.quit()