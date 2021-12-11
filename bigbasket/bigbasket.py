import json
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# TODO : handle logging
# TODO : remove elements which are ordered from file


def login(browser):
    browser.get('https://www.bigbasket.com/auth/login/')
    username = browser.find_element_by_id('otpEmail')
    username.send_keys('9374713635')
    browser.find_element_by_css_selector('button.btn.btn-default.login-btn').click()
    # otp flutter
    time.sleep(25)
    # print(str(datetime.datetime.now()), ' : Logged in')
    return


def search(browser, keyword):
    # print(str(datetime.datetime.now()), ' : Searching for ', keyword)
    search_box = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'input')))
    # print(str(datetime.datetime.now()), ' : Got search box')
    search_box.clear()
    # print(str(datetime.datetime.now()), ' : Search box cleared')
    search_box.send_keys(keyword)
    # print(str(datetime.datetime.now()), ' : Sent keys')
    search_ = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button.btn.btn-default.bb-search')))
    search_.click()
    # print(str(datetime.datetime.now()), ' : Search form submitted')
    return


def add_item(browser, quantity):
    # print(str(datetime.datetime.now()), ' : Adding item to cart')
    html_list = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button.btn.btn-add.col-xs-9')))
    html_list.click()
    if quantity > 1:
        for i in range(quantity - 1):
            html_list = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn.rt')))
            time.sleep(1.5)
            html_list.click()

    # print(str(datetime.datetime.now()), ' : Added {}'.format(quantity))
    return


def get_my_total(browser):
    # print(str(datetime.datetime.now()), ' : Getting total amount')
    my_total = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'finalTotal')))
    my_total = my_total.get_attribute('textContent')
    my_total = re.findall(r'\d+', my_total)
    my_total = float(my_total[0])
    return my_total,


def go_to_checkout(browser):
    # print(str(datetime.datetime.now()), ' : Going to the checkout page')
    browser.get('https://www.bigbasket.com/basket/?ver=1')
    return


def checkout(browser):
    # print(str(datetime.datetime.now()), ' : Checking out')
    checkout_button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'checkout')))
    time.sleep(1)
    checkout_button.click()
    return


def get_shopping_list():
    # print(str(datetime.datetime.now()), ': Getting shopping list')
    items = json.load(open('bigbasket/items.json'))
    shopping_list = []
    quantity_list = []
    for key in items.keys():
        shopping_list.append(items[key]['item'])
        quantity_list.append(int(items[key]['quantity']))
    return shopping_list, quantity_list



def main():
    # browser = webdriver.Chrome()
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    browser = webdriver.Chrome(options=options)
    browser.get('https://www.bigbasket.com/')
    # browser.get('https://www.bigbasket.com/auth/login/')
    # login(browser)
    shopping_list, quantity_list = get_shopping_list()
    shopping_list = [s.rstrip() for s in shopping_list]
    for item, quantity in zip(shopping_list, quantity_list):
        search(browser, item)
        add_item(browser, quantity)
        browser.get('https://www.bigbasket.com/')

    go_to_checkout(browser)
    # checkout(browser)
