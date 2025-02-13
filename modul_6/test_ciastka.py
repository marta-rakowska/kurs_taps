from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://fabrykatestow.pl")

driver.delete_all_cookies()

driver.add_cookie({"name": "test", "value": "value"})
driver.add_cookie({"name": "test2", "value": "value2"})

print(driver.get_cookies())

driver.delete_cookie("test")

print(driver.get_cookies())

driver.quit()