# usage: python complain.py [-h] [--headless] username password
#
# positional arguments:
#   username    Excitel username
#   password    Excitel password
#
# optional arguments:
#   -h, --help  show this help message and exit
#   --headless  Use Chrome in headless mode
#

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def login(driver, username, password):
    driver.get('https://my.excitel.com/login')
    username_element_path = '//form//input[@formcontrolname="username"]'
    WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, username_element_path))
    )
    username_element = driver.find_element_by_xpath(username_element_path)
    username_element.clear()
    username_element.send_keys(username)
    password_element = driver.find_element_by_xpath('//form//input[@formcontrolname="password"]')
    password_element.clear()
    password_element.send_keys(password)
    login_button_element = driver.find_element_by_xpath('//form//button')
    login_button_element.click()


def lodge_complaint(driver):
    WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'dashboard-title'))
    )
    WebDriverWait(driver, 30).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, 'loader-container'))
    )
    complaint_button_path = '//div[@class="dashboard-actions"]//button[@class="btn red connectivity-button"]'
    complaint_button_element = driver.find_element_by_xpath(complaint_button_path)
    complaint_button_element.click()

    confirm_button_element = driver.find_element_by_xpath('//modal-footer-actions/button[@class="btn green"]')
    confirm_button_element.click()


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('username', nargs='?', help='Excitel username')
    parser.add_argument('password', nargs='?', help='Excitel password')
    parser.add_argument('--headless', help='Use Chrome in headless mode', action='store_true')
    args = parser.parse_args()

    username = args.username
    password = args.password

    if(username is None or password is None):
        print('No credentials passed through command line. Looking for them in creds file.')
        try:
            with open("creds") as f:
                username = f.readline()[:-1]
                password = f.readline()
        except OSError as err:
            print('Credentials file not found!')
            print(err)
            exit()

    options = webdriver.ChromeOptions()
    if args.headless:
        options.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=options)
    print('Logging in...')
    login(driver, username, password)
    print("Logged in!")
    print("Lodging complaint...")
    lodge_complaint(driver)
    print("Complaint lodged!")
    driver.close()
