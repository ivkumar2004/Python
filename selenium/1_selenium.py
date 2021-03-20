from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager #only used to install the webdriver in runtime

# WebDriverManager to install and invoke the driver for Chrome/Firefox/IE
# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(executable_path = r'C:\Users\ivkum\AppData\Local\Programs\Python\Python38-32\chromedriver.exe')
driver.get("https://www.facebook.com")
driver.close()