from selenium import webdriver

username = ''
password = ''

driver = webdriver.Chrome()
driver.get('https://my.excitel.com/login')
username_element = driver.find_element_by_xpath('//form//input[@formcontrolname="username"]')
username_element.clear()
username_element.send_keys(username)
password_element = driver.find_element_by_xpath('//form//input[@formcontrolname="password"]')
password_element.clear()
password_element.send_keys(password)
login_button_element = driver.find_element_by_xpath('//form//button')
login_button_element.click()

# driver.close()