from helpers.support_functions import *


shop_page_header = '//*[@id="main"]/header/h1'
beanie_product_name = '//*[@id="main"]/ul/li[1]/a[1]/h2'
hoodie_product_name = '//*[@id="main"]/ul/li[4]/a[1]/h2'
first_page_button = '//*[@id="main"]/div[1]/nav/ul/li[1]/span'
first_page_button_when_on_second = '//*[@id="main"]/div[1]/nav/ul/li[2]/a'
second_page_button = '//*[@id="main"]/div[1]/nav/ul/li[2]/a'
previous_page_button = '//*[@id="main"]/div[1]/nav/ul/li[1]/a'
next_page_button = '//*[@id="main"]/div[1]/nav/ul/li[3]/a'
page_results_count = '//*[@id="main"]/div[1]/p'
close_message_button = '/html/body/p/a'


first_page_results_text = 'Wyświetlanie 1–8'
second_page_results_text = 'Wyświetlanie 9–11'


def shop_page_header_visible(driver_instance):
    wait_for_visibility_of_element(driver_instance, shop_page_header)
    elem = driver_instance.find_element(By.XPATH, shop_page_header)
    header_text = 'Sklep'
    if elem.text == header_text:
        return True
    else:
        return False


def go_to_beanie_page(driver_instance):
    elem = driver_instance.find_element(By.XPATH, close_message_button)
    elem.click()
    wait_for_visibility_of_element(driver_instance, beanie_product_name)
    elem2 = driver_instance.find_element(By.XPATH, beanie_product_name)
    elem2.click()


def go_to_hoodie_page(driver_instance):
    elem = driver_instance.find_element (By.XPATH, close_message_button)
    elem.click()
    wait_for_visibility_of_element(driver_instance, hoodie_product_name)
    elem2 = driver_instance.find_element(By.XPATH, hoodie_product_name)
    elem2.click()


def go_to_first_page(driver_instance):
    elem = driver_instance.find_element(By.XPATH, first_page_button_when_on_second)
    elem.click()


def first_page_visible(driver_instance):
    wait_for_visibility_of_element(driver_instance, page_results_count)
    elem = driver_instance.find_element(By.XPATH, page_results_count)
    if first_page_results_text in elem.text:
        return True
    else:
        return False


def go_to_second_page(driver_instance):
    elem = driver_instance.find_element(By.XPATH, second_page_button)
    elem.click()


def second_page_visible(driver_instance):
    wait_for_visibility_of_element(driver_instance, page_results_count)
    elem = driver_instance.find_element(By.XPATH, page_results_count)
    if second_page_results_text in elem.text:
        return True
    else:
        return False


def go_to_next_page(driver_instance):
    wait_for_visibility_of_element(driver_instance, next_page_button)
    elem = driver_instance.find_element(By.XPATH, next_page_button)
    elem.click()


def go_to_previous_page(driver_instance):
    elem = driver_instance.find_element(By.XPATH, previous_page_button)
    elem.click()



