#!/usr/bin/python3

######################################
# Selenium Python - Install Selenium, Chromedriver, Chrome on Ubuntu, Debian, Python - Part 1b
# https://youtu.be/67h3IT2lm40
# 0:00 - install Google Chrome browser from .deb source file
# 4:36 - skip this part - bad editing repeat of install Google Chrome
# 8:29 - install chromedriver
# 16:45 - install pip3
# 19:21 - install Selenium
# 20:21 - create a directory and python test script
# The last few minutes of the video was cut off (I should have checked after editing)
# I also did an initial part 1a for chromium browser instead of google-chrome. 
# For the full script and demo you can also follow Part 1a from here, https://youtu.be/_qd--H1jBbw?t=299 (script at 4 min 59 sec, and demo at 17 min 14 sec)
# Full continuation of the script and a demo can also be followed in Part 2: https://youtu.be/mU1gVBYFuOk (script at 7 min 29 sec)

# script: https://github.com/datyrlab/selenium-webdriver/blob/master/01-04-test-script.py

# if using google-chrome then:
# DRIVER_LOCATION = "/usr/bin/chromedriver"
# BINARY_LOCATION = "/usr/bin/google-chrome"

# if using chromium browser then:
# DRIVER_LOCATION = "/snap/bin/chromium.chromedriver"
# BINARY_LOCATION = "/usr/bin/chromium-browser"

# Beginner install Selenium Python on Ubuntu Debian, Chromium Browser - Part 1a
# https://youtu.be/_qd--H1jBbw
# Chromium is a preferred choice of browser for most Linux distros, 
# but if you prefer to install and use Google Chrome then follow Part 1b. 
# Google Chrome tends to be a little friendlier with minor aspects of automation that I'll cover later. 
# Note that Google Chrome is actually Chromium Browser but with Google's add-on's, snooping and personal stamp on it

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
