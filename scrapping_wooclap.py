import os
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


driver_path = "/Users/samain/projects/training/selenium_py/chromedriver/chromedriver"
print(driver_path)
os.environ["webdriver.chrome.driver"] = driver_path
# service = Service(executable_path='/Users/samain/projects/training/selenium_py/chromedriver/chromedriver')
service = Service(executable_path='./geckodriver')
driver = webdriver.Firefox(service=service)
# driver = webdriver.Chrome(service=service)
driver.get("https://www.wooclap.com/")

driver.quit()