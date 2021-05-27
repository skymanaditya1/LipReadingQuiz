from selenium import webdriver
import pandas as pd
from time import sleep
import requests
import os
import random

#URL = 'https://www.lipreading.org/lipreading-missing-words'
URL = 'https://www.lipreading.org'
driver_path = '/home/aditya/Downloads/chromedriver/chromedriver'
driver = webdriver.Chrome(driver_path)
driver.get(URL)

sleep(5)

#signin = driver.find_element_by_xpath('//a[contains(@href,"Sign In")]')
signin = driver.find_element_by_link_text('Sign In')
signin.click()
sleep(1)
email = driver.find_element_by_xpath("//input[@id='userid']")
email.send_keys('agarwal.aditya5592@gmail.com')
password = driver.find_element_by_xpath("//input[@id='passwordinput']")
password.send_keys('helloaditya123')
button_signin = driver.find_element_by_xpath("//button[@id='signin']")
button_signin.click()
driver.get('https://www.lipreading.org/lipreading-missing-words')
#signin = driver.find_element_by_xpath("//a[text()='Re-Call']")