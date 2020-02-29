from selenium import webdriver
import time
driver=webdriver.Chrome()
url="https://www.hepsiburada.com/"
driver.get(url)
time.sleep(1)
driver.maximize_window()

