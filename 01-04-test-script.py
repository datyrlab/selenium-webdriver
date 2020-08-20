#!/usr/bin/python3

######################################
# datyrlab
# Selenium Python - Install Selenium, Chromedriver, Chrome on Ubuntu, Debian, Python - Part 1
# https://youtu.be/67h3IT2lm40i

# https://twitter.com/datyrlab
######################################

from selenium import webdriver 

DRIVER_LOCATION = "/usr/bin/chromedriver" 
BINARY_LOCATION = "/usr/bin/google-chrome" 

# start selenium
options = webdriver.ChromeOptions() 
options.binary_location = BINARY_LOCATION 

driver = webdriver.Chrome(executable_path=DRIVER_LOCATION, options=options) 

driver.get("https://www.imdb.com") 
print(driver.page_source.encode('utf-8')) 

# close browser and quit driver
driver.close() 
driver.quit() 
