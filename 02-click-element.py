#!/usr/bin/python3

######################################
# datyrlab
# Selenium Python - Click a page element - Part 2
# https://youtu.be/mU1gVBYFuOk

# https://twitter.com/datyrlab
######################################

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

DRIVER_LOCATION= "/usr/bin/chromedriver"
BINARY_LOCATION = "/usr/bin/google-chrome"

# start selenum
options = webdriver.ChromeOptions()
options.binary_location = BINARY_LOCATION

driver = webdriver.Chrome(executable_path=DRIVER_LOCATION, options=options)

# home page
driver.get("https://www.imdb.com")
print("landing page --------->")
print("current_url", driver.current_url)
print("title", driver.title)

# click link to signin options page
WAIT_ELEMENT = 30
XPATH_VALUE = "//*[@id=\"imdbHeader\"]/div[2]/div[5]/a/div"
x = WebDriverWait(driver, WAIT_ELEMENT).until(EC.presence_of_element_located((By.XPATH, XPATH_VALUE)))
outerHTML = x.get_attribute('outerHTML')
print(outerHTML)
time.sleep(5)
x.click()

# driver is now on the signin options page
print("\n", "signin options page --------->")
print("current_url", driver.current_url)
print("title", driver.title)

# close browser and quit driver
driver.close()
driver.quit()
