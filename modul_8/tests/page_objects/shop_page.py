from helpers.support_functions import *


beanie_product_name = '//*[@id="main"]/ul/li[1]/a[1]/h2'
hoodie_product_name = '//*[@id="main"]/ul/li[4]/a[1]/h2'
first_page_button = '//*[@id="main"]/div[1]/nav/ul/li[1]/span'
second_page_button = '//*[@id="main"]/div[1]/nav/ul/li[2]/a'
previous_page_button = '//*[@id="main"]/div[1]/nav/ul/li[1]/a'
next_page_button = '//*[@id="main"]/div[1]/nav/ul/li[3]/a'
page_results_count = '//*[@id="main"]/div[1]/p'
page_2_breadcrumb = '//*[@id="page"]/div[1]/div/nav/text()'


first_page_results_text = 'Wyświetlanie 1–8'
second_page_results_text = 'Wyświetlanie 9–11'


def go_to_beanie_page(driver_instance):
    wait_for_visibility_of_element(driver_instance, beanie_product_name)
    elem = driver_instance.find_element(By.XPATH, beanie_product_name)
    elem.click()


def go_to_hoodie_page(driver_instance):
    wait_for_visibility_of_element(driver_instance, hoodie_product_name)
    elem = driver_instance.find_element(By.XPATH, hoodie_product_name)
    elem.click()


def go_to_first_page(driver_instance):
    elem = driver_instance.find_element(By.XPATH, first_page_button)
    elem.click()


def first_page_visible(driver_instance):
    wait_for_invisibility_of_element(driver_instance, page_2_breadcrumb)
    elem = driver_instance.find_element(By.XPATH, page_results_count)
    if elem.text == first_page_results_text:
        return True
    else:
        return False


def go_to_second_page(driver_instance):
    elem = driver_instance.find_element(By.XPATH, second_page_button)
    elem.click()


def second_page_visible(driver_instance):
    wait_for_visibility_of_element(driver_instance, page_2_breadcrumb)
    elem = driver_instance.find_element(By.XPATH, page_results_count)
    if elem.text == second_page_results_text:
        return True
    else:
        return False


def go_to_next_page(driver_instance):
    elem = driver_instance.find_element(By.XPATH, next_page_button)
    elem.click()


def go_to_previous_page(driver_instance):
    elem = driver_instance.find_element(By.XPATH, previous_page_button)
    elem.click()



