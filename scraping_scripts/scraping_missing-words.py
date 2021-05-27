from selenium import webdriver
import pandas as pd
from time import sleep
import requests
import os
import random

alphanumeric = 'abcdefghijklmnopqrstuvwzyz1234567890'
random_string = ''.join(alphanumeric[random.randint(0, len(alphanumeric)-1)] for i in range(5))
print(f'Random string : {random_string}')

driver_path = '/home/aditya/Downloads/chromedriver/chromedriver'
driver = webdriver.Chrome(driver_path)

# Code to login to the lipreading.org website 
def login():
	URL = 'https://www.lipreading.org'
	driver.get(URL)

	sleep(5)

	signin = driver.find_element_by_link_text('Sign In')
	signin.click()
	
	sleep(1)

	email = driver.find_element_by_xpath("//input[@id='userid']")
	email.send_keys('agarwal.aditya5592@gmail.com')
	password = driver.find_element_by_xpath("//input[@id='passwordinput']")
	password.send_keys('helloaditya123')

	button_signin = driver.find_element_by_xpath("//button[@id='signin']")
	button_signin.click()

# Comment this code if login is not required
login()

URL = 'https://www.lipreading.org/lipreading-missing-words'
driver.get(URL)
config_file = os.path.basename(URL) + '_' + random_string + '.txt'
base_dir = '/home/aditya/iiith/lipreading/wav2lip_website/lipreading_website/media/lipreading_org_videos/'

if not os.path.exists(base_dir):
	os.mkdir(base_dir)

dir_path = os.path.join(base_dir, os.path.basename(URL) + '_' + random_string)

if not os.path.exists(dir_path):
	os.mkdir(dir_path)

sleep(1)
print('Click the button to start the game')
driver.find_element_by_xpath("//button[@id='btn_gamestart']").click()

file_options = dict()

while True:
	sleep(3)
	try:
		content = driver.find_element_by_xpath("//*[@id='player_frame']/div/video")
	except: 
		print("Done parsing the page. Exiting")
		break
	video_url = content.get_attribute("src")
	print(video_url)
	filename = os.path.basename(video_url)
	r = requests.get(video_url, allow_redirects=True)
	open(os.path.join(dir_path, filename), 'wb').write(r.content)
	print(f'Video file {filename} downloaded successfully')

	# Get the question 
	# question = driver.find_element_by_xpath("//*[@id='player_frame']/br[2]").text
	# print(question)

	# Get the reference to the text box - enter some junk value 
	user_predicted = driver.find_element_by_xpath("//input[@id='user_predicted']")
	user_predicted.send_keys(random_string)

	# Click the enter button 
	user_enter = driver.find_element_by_xpath("//button[@id='user_enter']")
	user_enter.click()

	# Correct answer is displayed at the bottom - which is also the masked text 
	correct_answer = driver.find_element_by_xpath("//*[@id='results']").text
	correct_answer_ = correct_answer.split(' ')[1] # corresponds to the answer text
	print(f'Correct answer : {correct_answer_}')

	continue_button = driver.find_element_by_xpath("//*[@id='mcont']")
	continue_button.click()

	file_options[filename] = correct_answer_

print('Closing browser')
driver.close()

print(f'Writing to the config file : {config_file}')
# write the contents to the file 
with open(os.path.join(base_dir, config_file), 'w') as f:
	for filename in file_options.keys():
		f.write(os.path.join(os.path.basename(URL) + '_' + random_string, filename))
		f.write('\t' + file_options[filename])
		f.write('\n')