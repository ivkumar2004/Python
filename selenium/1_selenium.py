from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# WebDriverManager to install and invoke the driver for Chrome/Firefox/IE
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.facebook.com")
driver.close()