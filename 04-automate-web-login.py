#!/usr/bin/python3

######################################
# Selenium Python - Automate a login to a web site - Part 4
# https://youtu.be/Bw9ueo7qFmY
# 00:00 - intro
# 00:44 - copy and tidy script from previous tutorial. Plus, import module colorama
# 14:34 - continuing with automating the imdb.com website, code to click from sign-in option page to sign-in form
# 21:51 - code to automate completion of the sign-in form page. Form fields email, password and submit button
# 34:23 - run partial code to test click from the sign-in option page to sign-in form
# 39:24 - run full code, successful login to the imdb.com website

# script: https://github.com/datyrlab/selenium-webdriver/blob/master/04-automate-web-login.py

# install dependancies
# sudo pip3 install colorama
# sudo pip3 install pyvirtualdisplay

# Selenium Python - Run remote headless and screenshot a full web page - Part 3.2
# https://youtu.be/IT4aiNxWYEw

# https://twitter.com/datyrlab
######################################

from colorama import init
from colorama import Fore, Back, Style
init(autoreset=True)

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pyvirtualdisplay import Display
import time

DRIVER_LOCATION = "/usr/bin/chromedriver"
BINARY_LOCATION = "/usr/bin/google-chrome"

DISPLAY_VISIBLE = 1
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
title=driver.title
print(Fore.WHITE + Back.RED + f"1.1 - home page")
print(Fore.CYAN + Back.WHITE + f"current_url: {driver.current_url}")
print(Fore.MAGENTA + Back.WHITE + f"title: {title}")

# 1.2 take a screenshot
filename = f"/home/piuser/Desktop/tutorial/sel/screenshot/01.2-{title}.png"
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
title=driver.title
print(Fore.WHITE + Back.RED + f"2.1 - signin options page")
print(Fore.CYAN + Back.WHITE + f"current_url: {driver.current_url}")
print(Fore.MAGENTA + Back.WHITE + f"title: {title}")

# 2.2 take a screenshot
#time.sleep(5)
#filename = f"/home/piuser/Desktop/tutorial/sel/screenshot/02.2-{title}.png"
#driver.save_screenshot(filename)

# 2.3 click button to signin form 
XPATH_VALUE = "//*[@id=\"signin-options\"]/div/div[1]/a[1]/span[2]"
x = WebDriverWait(driver, WAIT_ELEMENT).until(EC.presence_of_element_located((By.XPATH, XPATH_VALUE)))
outerHTML = x.get_attribute('outerHTML')
print(outerHTML)
time.sleep(5)
x.click()

# 3.1 driver is now on the signin form page
print(Fore.WHITE + Back.RED + f"3.1 - signin form page")
print(Fore.CYAN + Back.WHITE + f"current_url: {driver.current_url}")
print(Fore.MAGENTA + Back.WHITE + f"title: {driver.title}")

# 3.2.1 complete the form fields

EMAIL_XPATH = "//*[@id=\"ap_email\"]"
EMAIL_VALUE = "YOUR-EMAIL"
PASSWORD_XPATH = "//*[@id=\"ap_password\"]"
PASSWORD_VALUE = "YOUR-PASSWORD"
SUBMIT_XPATH = "//*[@id=\"signInSubmit\"]"

# email 
x = WebDriverWait(driver, WAIT_ELEMENT).until(EC.presence_of_element_located((By.XPATH, EMAIL_XPATH)))
x.send_keys(EMAIL_VALUE)
print(Fore.BLACK + Back.YELLOW + f"email form field: {x.get_attribute('outerHTML')}")
time.sleep(2)
x.send_keys()

# password 
x = WebDriverWait(driver, WAIT_ELEMENT).until(EC.presence_of_element_located((By.XPATH, PASSWORD_XPATH)))
x.send_keys(PASSWORD_VALUE)
print(Fore.BLACK + Back.YELLOW + f"password form field: {x.get_attribute('outerHTML')}")
time.sleep(2)
x.send_keys()

# 3.2.2 submit the form 
x = WebDriverWait(driver, WAIT_ELEMENT).until(EC.presence_of_element_located((By.XPATH, SUBMIT_XPATH)))
print(Fore.BLACK + Back.YELLOW + f"submit button: {x.get_attribute('outerHTML')}")
time.sleep(2)
x.click()

time.sleep(10)

# close browser, quit driver and stop display
driver.close()
driver.quit()
display.stop()
