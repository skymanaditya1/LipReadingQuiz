from selenium import webdriver
import pandas as pd
from time import sleep
import requests
import os
import random

alphanumeric = 'abcdefghijklmnopqrstuvwzyz1234567890'
random_string = ''.join(alphanumeric[random.randint(0, len(alphanumeric))] for i in range(5))
print(f'Random string : {random_string}')

URL = 'https://www.lipreading.org/consonants-eyedrills'
driver_path = '/home/aditya/Downloads/chromedriver/chromedriver'
driver = webdriver.Chrome(driver_path)
driver.get(URL)
config_file = os.path.basename(URL) + '_' + random_string + '.txt'
base_dir = '/home/aditya/iiith/lipreading/wav2lip_website/lipreading_website/media/lipreading_org_videos/'

if not os.path.exists(base_dir):
	os.mkdir(base_dir)

dir_path = os.path.join(base_dir, os.path.basename(URL) + '_' + random_string)

if not os.path.exists(dir_path):
	os.mkdir(dir_path)

sleep(5)
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

	try:
		answer_list = driver.find_element_by_xpath("//*[@id='cgame_main']/section/div[2]/div[2]/ul")
	except:
		break

	options = answer_list.find_elements_by_tag_name("li")
	answer_choices = list()
	for option in options:
		print(option.text)
		answer_choices.append(option.text)

	try:
		for option in options:
			option.click()
	except:
		print("Element not found exception")

	file_options[filename] = answer_choices

print('Closing browser')
driver.close()

# Write the file_options dictionary to a file
print(f'Writing to file : {config_file}')
with open(os.path.join(base_dir, config_file), 'w') as f:
	for filename in file_options.keys():
		f.write(os.path.join(os.path.basename(URL) + '_' + random_string, filename))
		for answer_choices in file_options[filename]:
			f.write('\t' + answer_choices)
		f.write('\n')