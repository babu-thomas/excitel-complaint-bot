from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.python.org")
driver.close()
