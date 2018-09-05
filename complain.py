from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def login(driver, username, password):
    driver.get('https://my.excitel.com/login')
    username_element = driver.find_element_by_xpath('//form//input[@formcontrolname="username"]')
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
    username = ''
    password = ''

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=options)
    print('Logging in...')
    login(driver, username, password)
    print("Logged in!")
    print("Lodging complaint...")
    lodge_complaint(driver)
    print("Complaint lodged!")
    driver.close()
