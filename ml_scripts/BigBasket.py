from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
from selenium.webdriver.common.action_chains import ActionChains
import os
import time
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# TODO : handle logging
# TODO : remove elements which are ordered from file
# TODO : add quantities of items to buy 								####done####

def login(browser):
    browser.get('https://www.bigbasket.com/auth/login/')
    username = browser.find_element_by_id('otpEmail')
    username.send_keys('9374713635')
    browser.find_element_by_css_selector('button.btn.btn-default.login-btn').click()
    ################################ otp flutter #########################################
    time.sleep(20)
    print(str(datetime.datetime.now()), ' : Logged in')
    return


def search(browser, keyword):
    print(str(datetime.datetime.now()), ' : Searching for ', keyword)
    search_box = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'input')))
    print(str(datetime.datetime.now()), ' : Got search box')
    search_box.clear()
    print(str(datetime.datetime.now()), ' : Search box cleared')
    search_box.send_keys(keyword)
    print(str(datetime.datetime.now()), ': Sent keys')
    search = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button.btn.btn-default.bb-search')))
    search.click()
    print(str(datetime.datetime.now()), ' : Search form submitted')
    return


def add_item(browser, quantity):
    print(str(datetime.datetime.now()), ' : Adding item to cart')
    html_list = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button.btn.btn-add.col-xs-9')))
    html_list.click()
    if quantity > 1:
        for i in range(quantity - 1):
            html_list = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn.rt')))
            time.sleep(1.5)
            html_list.click()
    return


def get_my_total(browser):
    print(str(datetime.datetime.now()), ' : Getting total amount')
    my_total = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'finalTotal')))
    my_total = my_total.get_attribute('textContent')
    my_total = re.findall(r'\d+', my_total)
    my_total = float(my_total[0])
    return my_total


def go_to_checkout(browser):
    print(str(datetime.datetime.now()), ' : Going to the checkout page')
    browser.get('https://www.bigbasket.com/basket/?ver=1')
    return


def checkout(browser):
    print(str(datetime.datetime.now()), ' : Checking out')
    checkout_button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'checkout')))
    time.sleep(1)
    checkout_button.click()
    return


def get_shopping_list():
    print(str(datetime.datetime.now()), ': Getting shopping list')
    with open('shopping_list', 'r') as f:
        f1 = f.readlines()
        shopping_list = []
        quantity_list = []
        for line in f1:
            shopping_list.append(line.split()[0])
            quantity_list.append(int(line.split()[1]))
    return shopping_list, quantity_list


def add(item):
    print(str(datetime.datetime.now()), ' : Adding item to shopping list')
    f = open('shopping_list', 'a')
    item = item + '\n'
    f.write(item)
    f.close()
    return


if __name__ == '__main__':
    browser = webdriver.Chrome()
    # options = webdriver.ChromeOptions()
    # options.add_argument("headless")
    # browser = webdriver.Chrome(options=options)
    browser.get('https://www.bigbasket.com/')
    browser.get('https://www.bigbasket.com/auth/login/')
    login(browser)
    shopping_list, quantity_list = get_shopping_list()
    shopping_list = [s.rstrip() for s in shopping_list]
    for item, quantity in zip(shopping_list, quantity_list):
        search(browser, item)
        add_item(browser, quantity)
        browser.get('http://www.bigbasket.com/')

    go_to_checkout(browser)
    time.sleep(1)
    checkout(browser)
    print('DONE')
