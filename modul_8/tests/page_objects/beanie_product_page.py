from datetime import datetime
from selenium.webdriver.common.keys import Keys

from helpers.support_functions import *

beanie_page_header = '//*[@id="product-46"]/div[2]/h1'
add_to_cart_button = '//*[@id="product-46"]/div[2]/form/button'
added_to_cart_alert = '//*[@id="content"]/div/div[1]/div'
quantity_input = 'quantity'
description_tab = '//*[@id="tab-title-description"]/a'
description_tab_header = '//*[@id="tab-description"]/h2'
additional_information_tab = '//*[@id="tab-title-additional_information"]/a'
additional_information_tab_header = '//*[@id="tab-additional_information"]/h2'
reviews_tab = '//*[@id="tab-title-reviews"]/a'
reviews_tab_header = '//*[@id="comments"]/h2'
fifth_star = '//*[@id="commentform"]/div/p/span/a[5]'
review_input = '//*[@id="comment"]'
author_name_input = '//*[@id="author"]'
author_email_input = '//*[@id="email"]'
submit_button = '//*[@id="submit"]'
add_review_error_message = 'wp-die-message'
beanie_color = '//*[@id="tab-additional_information"]/table/tbody/tr/td/p'
comment_awaiting_approval = '//*[@id="comment-2477"]/div/p/em'
added_review = '//*[@id="comment-2477"]/div'


author_name = 'Cotaga'
author_email = 'cotaga1249@maillei.net'
add_review_error_message_text = 'proszę wypełnić wymagane pola'


def beanie_header_visible(driver_instance):
    wait_for_visibility_of_element(driver_instance, beanie_page_header)
    elem = driver_instance.find_element(By.NAME, beanie_page_header)
    header_text = 'Beanie'
    if elem.text == header_text:
        return True
    else:
        return False


def change_quantity_to_2(driver_instance):
    elem = driver_instance.find_element(By.NAME, quantity_input)
    # elem.clear()
    # elem.send_keys(2)
    elem.send_keys(Keys.ARROW_UP)


def add_to_cart(driver_instance):
    elem = driver_instance.find_element(By.XPATH, add_to_cart_button)
    elem.click()


def added_to_cart_alert_displayed(driver_instance):
    wait_for_visibility_of_element(driver_instance, added_to_cart_alert)
    elem = driver_instance.find_element(By.XPATH, added_to_cart_alert)
    elem.is_displayed()


def go_to_description_tab(driver_instance):
    elem = driver_instance.find_element(By.XPATH, description_tab)
    elem.click()


def description_tab_header_visible(driver_instance):
    wait_for_visibility_of_element(driver_instance, description_tab_header)
    elem = driver_instance.find_element(By.XPATH, description_tab_header)
    elem.is_displayed()


def go_to_additional_information_tab(driver_instance):
    elem = driver_instance.find_element(By.XPATH, additional_information_tab)
    elem.click()


def additional_information_tab_header_visible(driver_instance):
    wait_for_visibility_of_element(driver_instance, additional_information_tab_header)
    elem = driver_instance.find_element(By.XPATH, additional_information_tab_header)
    tab_header_text = 'Informacje dodatkowe'
    if elem.text == tab_header_text:
        return True
    else:
        return False


def go_to_reviews_tab(driver_instance):
    elem = driver_instance.find_element(By.XPATH, reviews_tab)
    elem.click()


def reviews_tab_header_visible(driver_instance):
    wait_for_visibility_of_element(driver_instance, reviews_tab_header)
    elem = driver_instance.find_element(By.XPATH, reviews_tab_header)
    reviews_tab_header_text = 'Opinie'
    if elem.text in reviews_tab_header_text:
        return True
    else:
        return False


def add_five_stars_rating(driver_instance):
    elem = driver_instance.find_element(By.XPATH, fifth_star)
    elem.click()


def add_review_text(driver_instance):
    elem = driver_instance.find_element(By.XPATH, review_input)
    elem.send_keys(str(datetime.now()))


def add_author_name(driver_instance):
    elem = driver_instance.find_element(By.XPATH, author_name_input)
    elem.send_keys(author_name)


def add_author_email(driver_instance):
    elem = driver_instance.find_element(By.XPATH, author_email_input)
    elem.send_keys(author_email)


def submit_review(driver_instance):
    elem = driver_instance.find_element(By.XPATH, submit_button)
    elem.click()


def add_valid_review(driver_instance):
    add_five_stars_rating(driver_instance)
    add_review_text(driver_instance)
    add_author_name(driver_instance)
    add_author_email(driver_instance)
    submit_review(driver_instance)


def add_empty_review(driver_instance):
    submit_review(driver_instance)


def add_review_without_rating(driver_instance):
    add_review_text(driver_instance)
    add_author_name(driver_instance)
    add_author_email(driver_instance)
    submit_review(driver_instance)


def add_review_without_text(driver_instance):
    add_five_stars_rating(driver_instance)
    add_author_name(driver_instance)
    add_author_email(driver_instance)
    submit_review(driver_instance)


def add_review_without_author_name(driver_instance):
    add_five_stars_rating(driver_instance)
    add_review_text(driver_instance)
    add_author_email(driver_instance)
    submit_review(driver_instance)


def add_review_without_author_email(driver_instance):
    add_five_stars_rating(driver_instance)
    add_review_text(driver_instance)
    add_author_name(driver_instance)
    submit_review(driver_instance)


def add_review_error_message_visible(driver_instance):
    wait_for_visibility_of_element_by_class(driver_instance, add_review_error_message)
    elem = driver_instance.find_element(By.CLASS_NAME, add_review_error_message)
    if elem.is_displayed():
        return True
    else:
        return False


def added_comment_visible(driver_instance):
    wait_for_visibility_of_element_by_class(driver_instance, 'comment_container')
    elem = driver_instance.find_element(By.CLASS_NAME, 'comment_container')
    if elem.is_displayed():
        return True
    else:
        return False


# def accept_alert(driver_instance):
#     try:
#         alert = driver_instance.switch_to.alert
#         alert.accept()
#         return 'Alert accepted'
#     except NoAlertPresentException:
#         return False


def missing_rating_alert_displayed(driver_instance):
    try:
        alert = driver_instance.switch_to.alert
        alert_text = 'Proszę wybrać ocenę'
        if alert_text in alert.text:
            return True
    except NoAlertPresentException:
        return False


def two_products_added_to_cart_info_displayed(driver_instance):
    wait_for_visibility_of_element(driver_instance, added_to_cart_alert)
    elem = driver_instance.find_element(By.XPATH, added_to_cart_alert)
    info_text = '2 × „Beanie” zostało dodanych do koszyka.'
    if info_text in elem.text:
        return True
    else:
        return False














