#!/usr/bin/python3

######################################
# Selenium Python - Run remote headless and screenshot a full web page - Part 3.2
# https://youtu.be/IT4aiNxWYEw
# 00:00 - intro
# 01:25 - copy python script from last screenshot tutorial
# 02:30 - update script, import module pyvirtualdisplay to run Selenium as headless
# 04:19 - create a pyvirtualdisplay instance, configure settings to enable/ disable headless and create a custom screen size 
# 09:03 - run script with virtual display in visible mode
# 10:54 - run script with virtual display in headless mode (raising error dependant library Xvfb missing)
# 11:35 - install dependant library Xvfb required to run pyvirtualdisplay in headless mode
# 13:05 - run script with virtual display in headless mode for successful full length web page screenshot

# script: https://github.com/datyrlab/selenium-webdriver/blob/master/03-02-headless-screenshot-full-page.py

# Selenium Python - Automate a screenshot of a web page - Part 3.1
# https://youtu.be/5douXMrgTfM

# https://twitter.com/datyrlab
######################################

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pyvirtualdisplay import Display 
import time

DRIVER_LOCATION = "/usr/bin/chromedriver"
BINARY_LOCATION = "/usr/bin/google-chrome"


DISPLAY_VISIBLE = 0
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 3000

# start display 
display = Display(visible=DISPLAY_VISIBLE, size=(DISPLAY_WIDTH, DISPLAY_HEIGHT))
display.start()

# start selenium
options = webdriver.ChromeOptions()
options.binary_location = BINARY_LOCATION

driver = webdriver.Chrome(executable_path=DRIVER_LOCATION, options=options)

# 1.1 home page
driver.get("https://www.imdb.com")
print("landing page --------->")
print("current_url", driver.current_url)
title=driver.title
print("title: ", title)

# 1.2 take a screenshot
filename = f"/home/piuser/Desktop/tutorial/sel/screenshot/{title}.png"
driver.save_screenshot(filename)

# 1.3 click link to signin options page
WAIT_ELEMENT = 30
XPATH_VALUE = "//*[@id=\"imdbHeader\"]/div[2]/div[5]/a/div"
x = WebDriverWait(driver, WAIT_ELEMENT).until(EC.presence_of_element_located((By.XPATH, XPATH_VALUE)))
outerHTML = x.get_attribute('outerHTML')
print(outerHTML)
time.sleep(5)
x.click()

# 2.1 driver is now on the signin options page
print("\n", "signin options page --------->")
print("current_url", driver.current_url)
title=driver.title
print("title: ", title)

# 2.2 take a screenshot
time.sleep(5)
filename = f"/home/piuser/Desktop/tutorial/sel/screenshot/{title}.png"
driver.save_screenshot(filename)

# close browser and quit driver
driver.close()
driver.quit()
display.stop()
