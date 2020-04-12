from scrapy import Selector
from urllib import request
import pandas as pd
import time

def save_to_html(data):
	f = open('drop.html', 'w+')
	f.write(str(data[0]))

def get_categories():
	url = 'https://nofluffjobs.com/'
	html = request.urlopen(url)
	sel = Selector(text=html.read(), type="html")
	category_names = []
	category_urls = []
	name_xpath = '//nfj-postings-list[@style!="min-height:0px;"]/div/h1/a/text()[1]'
	url_xpath = '//nfj-postings-list[@style!="min-height:0px;"]/div/h1/a/@href'

	category_names = [category_name.strip() for category_name in sel.xpath(name_xpath).getall()]
	category_urls =  ['https://nofluffjobs.com' + category_url for category_url in sel.xpath(url_xpath).getall()]

	return category_urls 
	# print(category_urls)

def get_offers_url(url=None):

	with open('offers_url.txt', 'a') as f:
		try:
			html = request.urlopen(url)
			sel = Selector(text=html.read(), type="html")
			urls=[]

			xpath = '//nfj-main-content//nfj-postings-item//@href'
			offers_url = ['https://nofluffjobs.com' + offer_url for offer_url in sel.xpath(xpath).getall()]

			# return offers_url
			f.writelines([url + '\n' for url in offers_url])
		except:
			print(url)


if __name__ == '__main__':
	with open('offers_url.txt', 'w') as f:
		pass

	for category_url in get_categories():
		get_offers_url(category_url)
		time.sleep(1)


