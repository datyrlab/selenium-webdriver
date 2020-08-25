#!/usr/bin/python3

######################################
# Selenium Python - Click a page element - Part 2
# https://youtu.be/mU1gVBYFuOk
# 0:00 - intro
# 0:36 - get the XPath value from a web page (XPath is like a coordinate location of a link or element that you want to click)
# 3:55 - copy script from previous tutorial
# 6:58 - quick recap of script from previous tutorial
# 9:24 - update to script begins here 
# 9:46 - import from Selenium required modules
# 15:33 - add code to click element
# 26:30 - run the script

# script: https://github.com/datyrlab/selenium-webdriver/blob/master/02-click-element.py

# Beginner install Selenium Python on Ubuntu Debian, Chromium Browser - Part 1a
# https://youtu.be/_qd--H1jBbw
# Chromium is a preferred choice of browser for most Linux distros, 
# but if you prefer to install and use Google Chrome then follow Part 1b. 
# Google Chrome tends to be a little friendlier with minor aspects of automation that I'll cover later. 
# Note that Google Chrome is actually Chromium Browser but with Google's add-on's, snooping and personal stamp on it

# Selenium Python - Install Selenium, Chromedriver, Chrome on Ubuntu, Debian, Python - Part 1b
# https://youtu.be/67h3IT2lm40

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
