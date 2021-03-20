from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# from webdriver_manager.chrome import ChromeDriverManager #only used to install the webdriver in runtime
## WebDriverManager to install and invoke the driver for Chrome/Firefox/IE
# driver = webdriver.Chrome(ChromeDriverManager().install())

# To disable the browser notifications
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('--disable-notifications')

driverPath = r'C:\Users\ivkum\AppData\Local\Programs\Python\Python38-32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driverPath, options=chromeOptions)
driver.get("https://www.facebook.com")

# Sending user name
userName = 'ivkumar2004@gmail.com'
userNameXpath = "//*[@type='text' and @name='email' and contains(@class,'inputtext')]"
userElement = driver.find_element_by_xpath(userNameXpath)
userElement.send_keys(userName)

# Sending password
passWord = 'il0vey0u@1'
passWordXpath = "//input[@type='password' and @name='pass' and contains(@class,'inputtext')]"
passWordElement = driver.find_element_by_xpath(passWordXpath)
passWordElement.send_keys(passWord)

# Clicking submit
submitXpath = "//button[@name='login' and @type='submit' and text()='Log In']"
submitElement = driver.find_element_by_xpath(submitXpath)
submitElement.click()
sleep(15)

# Checking page moved to user welcome screen
welcomeTextXpath = "//span[contains(text(),'Welcome to Facebook, ')] "
welcomeTextElement = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, welcomeTextXpath)))

# Closing the browser
driver.close()
