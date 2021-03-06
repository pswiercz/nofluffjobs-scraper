import time
import datetime
from datetime import date
from os import listdir
import scrapy
from scrapy import Selector
from urllib import request

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains


MAX_100_PAGES = False
# PROFILE_NAME = 'java in warsaw for expert and serior with gym'
PROFILE_NAME = 'python job in warsaw'

class url_item(scrapy.Item):
    url = scrapy.Field()

class UrlListSpider(scrapy.Spider):
    name = 'url_lists'

    def parse(self, response):
        xpath = '//nfj-search-results//nfj-postings-list//nfj-postings-item/a/@href'
        selection = response.xpath(xpath)
        for s in selection:
            l = url_item()
            l['url'] = s.get()
            yield dict(l)

def get_profile(profile_selected):
	with open('profiles.txt', 'r') as file_profiles:
		all_profiles = file_profiles.read().splitlines()

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

			if p_key == 'seniority': # validation of seniority category data
				p_values = [item.lstrip().rstrip() if item.lstrip().rstrip() in ['Trainee', 'Junior', 'Mid', 'Senior', 'Expert'] 
							else None for item in p_value_raw.split(',')]
			else:  
				p_values = [None if item.lstrip().rstrip() == '' else item.lstrip().rstrip() for item in p_value_raw.split(',') ]

			profile[p_key] = p_values
	return profile

def set_technology(category_items):
	if category_items[0]:
		# get to category menu
		driver.find_element_by_xpath('//nfj-controls-toolbar//span[text()="Technology"]//parent::*').click()
		time.sleep(1)

		# filling search form
		for category in category_items:
			driver.find_element_by_xpath('//nfj-filter-custom-control//input[@placeholder="Add custom"]').send_keys(category)
			time.sleep(1)
			driver.find_element_by_xpath('//nfj-filter-custom-control//button[text()=" + "]').click()
			time.sleep(1)

		driver.find_element_by_xpath('//nfj-filters-wrapper//button[text()=" Apply "]').click()

def set_location(category_items):
	if category_items[0]:
 		# get to category menu
		driver.find_element_by_xpath('//nfj-controls-toolbar//span[text()=" Location"]//parent::*').click()
		time.sleep(1)

		# filling search form
		for category in category_items:
			driver.find_element_by_xpath('//nfj-filter-custom-control//input[@placeholder="Add custom"]').send_keys(category)
			time.sleep(1)
			driver.find_element_by_xpath('//nfj-filter-custom-control//button[text()=" + "]').click()
			time.sleep(1)

		driver.find_element_by_xpath('//nfj-filters-wrapper//button[text()=" Apply "]').click()

def set_job_category(category_items):
	if category_items[0]:
 		# get to category menu
		driver.find_element_by_xpath('//nfj-controls-toolbar//span[text()="Category"]//parent::*').click()
		time.sleep(1)

		# filling search form
		for category in category_items:
			try:
				driver.find_element_by_xpath(f'//ngb-popover-window//nfj-filters-wrapper//button[contains(text(), "{category}")]').click()
				time.sleep(1)
			except:
				print(category, ' was not found')

		driver.find_element_by_xpath('//nfj-filters-wrapper//button[text()=" Apply "]').click()

def set_more_custom(more_custom_items, seniority_items):
	if more_custom_items[0] or seniority_items[0]:
 		# get to category menu
		driver.find_element_by_xpath('//nfj-controls-toolbar//span[text()="More"]//parent::*').click()
		time.sleep(1)

		# filling search form
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

def accept_coockies():
	try:
		driver.find_element_by_xpath('//nfj-fixed-banner//button').click()
	except:
		pass

def change_lang():
	driver.find_element_by_xpath('//nfj-navbar-language-picker').click()
	time.sleep(1)
	driver.find_element_by_xpath('//nfj-navbar-language-picker//li//img[@src="/assets/images/flags-countries/EN.svg"]').click()
	time.sleep(1)

def get_urls():
	offers_url = []
	page_number = 1
	ins = UrlListSpider()

	while True:
		sel = Selector(text=driver.page_source, type="html")
		gen = ins.parse(sel)
		for item in gen:
			offers_url.append(item['url'])

		try: # move to next page
			driver.find_element_by_xpath('//nfj-main-loader//nfj-search-results//div//li[@class="page-item"]\
										  //a[@aria-label="Next"]//parent::*').click()
			time.sleep(2)
		except:
			break

		# stop moving to next page if MAX_100_PAGES is True
		if page_number > 4 and MAX_100_PAGES:
			break
		page_number += 1

	return offers_url

def save_urls(urls, profile_name):
	# Getting last index of urls file for new one
	urls_names = listdir('urls')
	max_number = []
	for item in urls_names:
		num, *_ = item.split('_')
		try:
			num = int(num)
		except:
			continue

		max_number.append(num)

	if max_number:
		max_number = max(max_number) + 1
	else:
		max_number = 1

	# saving url
	t = time.localtime()
	with open(f"urls//{max_number}_urls_{profile_name[0]}_{date.today()}_{time.strftime('%H-%M-%S', t)}.txt", 'w+') as f:
		f.writelines(['https://nofluffjobs.com' + url + '\n' for url in urls])

if __name__ == '__main__':
	url = 'https://nofluffjobs.com/jobs'
	service = Service('/usr/bin/chromedriver')
	service.start()
	driver = webdriver.Remote(service.service_url)
	driver.get(url)

	profile = get_profile(PROFILE_NAME)

	time.sleep(2)
	accept_coockies()
	time.sleep(1)
	change_lang()
	time.sleep(1)

	# set up search form
	set_technology(profile['technology'])
	set_location(profile['location'])
	set_job_category(profile['category'])
	set_more_custom(more_custom_items = profile['more_custom'], seniority_items = profile['seniority'])

	time.sleep(1)

	# check if page display any offer
	try:
		driver.find_element_by_xpath('//nfj-no-offers-found-header//h2[text()=" No job offers found. "]').get_attribute('innerHTML')
		print('no offers has been found')
	except:
		accept_coockies()
		# save urls file
		save_urls(get_urls(), profile['profile_name'])