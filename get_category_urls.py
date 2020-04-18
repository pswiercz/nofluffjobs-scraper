from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time
import getpass
import datetime
from scrapy import Selector
from urllib import request
		# actions = ActionChains(driver)
		# actions.send_keys(u'\ue00c')
		# actions.perform()
# print(driver.find_element_by_xpath('//nfj-controls-toolbar//span[text()="Technology +"]//parent::*').get_attribute('innerHTML'))

def get_profile(profile_selected):
	with open('profiles.txt', 'r') as file_profiles:
		all_profiles = file_profiles.read().splitlines()

	profile_selected = 'first'
	profile = {'profile_name': '', 'technology': [], 'location': [], 'category': [], 'more_custom': [], 'seniority': []}
	right_name = False

	for profiles_row in all_profiles:
		if profiles_row == '-' and right_name:
			break

		if (profiles_row == 'profile_name:' + profile_selected or right_name) and profiles_row: 
			right_name = True
			p_values = []
			p_key, p_value_raw = profiles_row.split(':') 
			p_key = p_key.lstrip().rstrip()

			if p_key == 'seniority':
				p_values = [item.lstrip().rstrip() if item.lstrip().rstrip() in ['Trainee', 'Junior', 'Mid', 'Senior', 'Expert'] 
							else None for item in p_value_raw.split(',')]
			else:  
				p_values = [None if item.lstrip().rstrip() == '' else item.lstrip().rstrip() for item in p_value_raw.split(',') ]

			profile[p_key] = p_values
	return profile


def set_technology(category_items):
	if category_items[0]:
# 		# get to category menu
		driver.find_element_by_xpath('//nfj-controls-toolbar//span[text()="Technology +"]//parent::*').click()
		time.sleep(1)

		for category in category_items:
			driver.find_element_by_xpath('//nfj-filter-custom-control//input[@placeholder="Add custom"]').send_keys(category)
			time.sleep(1)
			driver.find_element_by_xpath('//nfj-filter-custom-control//button[text()=" + "]').click()
			time.sleep(1)

		driver.find_element_by_xpath('//nfj-filters-wrapper//button[text()=" Apply "]').click()

def set_location(category_items):
	if category_items[0]:
# 		# get to category menu
		driver.find_element_by_xpath('//nfj-controls-toolbar//span[text()=" Location +"]//parent::*').click()
		time.sleep(1)

		for category in category_items:
			driver.find_element_by_xpath('//nfj-filter-custom-control//input[@placeholder="Add custom"]').send_keys(category)
			time.sleep(1)
			driver.find_element_by_xpath('//nfj-filter-custom-control//button[text()=" + "]').click()
			time.sleep(1)

		driver.find_element_by_xpath('//nfj-filters-wrapper//button[text()=" Apply "]').click()

def set_job_category(category_items):
	if category_items[0]:
# 		# get to category menu
		driver.find_element_by_xpath('//nfj-controls-toolbar//span[text()="Category +"]//parent::*').click()
		time.sleep(1)

		for category in category_items:
			try:
				driver.find_element_by_xpath(f'//ngb-popover-window//nfj-filters-wrapper//button[contains(text(), "{category}")]').click()
				time.sleep(1)
			except:
				print(category, ' was not found')

		driver.find_element_by_xpath('//nfj-filters-wrapper//button[text()=" Apply "]').click()

def set_more_custom(more_custom_items, seniority_items):
	if more_custom_items[0] or seniority_items[0]:
# 		# get to category menu
		driver.find_element_by_xpath('//nfj-controls-toolbar//span[text()="More +"]//parent::*').click()
		time.sleep(1)

		if more_custom_items[0]:
			for item in more_custom_items:
				driver.find_element_by_xpath('//nfj-filter-custom-control//input[@placeholder="Add custom"]').send_keys(item)
				time.sleep(1)
				driver.find_element_by_xpath('//nfj-filter-custom-control//button[text()=" + "]').click()
				time.sleep(1)

		if seniority_items[0]:
			for item in seniority_items:
				driver.find_element_by_xpath(f'//ngb-popover-window//label[contains(text(), "{item}")]').click()
				time.sleep(1)

		driver.find_element_by_xpath('//nfj-filters-wrapper//button[text()=" Apply "]').click()
# 	print(drop)

def change_lang():
	driver.find_element_by_xpath('//nfj-navbar-language-picker').click()
	time.sleep(1)
	driver.find_element_by_xpath('//nfj-navbar-language-picker//li//img[@src="/assets/images/flags-countries/EN.svg"]').click()
	time.sleep(1)

def get_urls():
	offers_url = []

	# while True
	html = driver.find_element_by_xpath('//nfj-main-content').get_attribute('innerHTML')
	sel = Selector(text=html, type="html")
	xpath = '//nfj-main-loader//nfj-postings-list//nfj-postings-item//a//@href'
	offers_url.append(*sel.xpath(xpath).getall())
	print(offers_url)

url = 'https://nofluffjobs.com/jobs'
service = Service('/usr/bin/chromedriver')
service.start()
driver = webdriver.Remote(service.service_url)
driver.get(url)

profile = get_profile('first')

time.sleep(2)
print(profile)

change_lang()
set_technology(profile['technology'])
set_location(profile['location'])
set_job_category(profile['category'])
set_more_custom(more_custom_items = profile['more_custom'], seniority_items = profile['seniority'])

# check if page dispaly any offer
time.sleep(1)
try:
	print(driver.find_element_by_xpath('//nfj-no-offers-found-header//h2[text()=" No job offers found. "]').get_attribute('innerHTML'))
except:
	print('page is ok')
	get_urls()
