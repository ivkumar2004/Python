from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://www.facebook.com")
time.sleep(1000)
driver.close()
