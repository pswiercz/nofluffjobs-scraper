from scrapy import Selector
from urllib import request
import pandas as pd
import time
from tqdm import tqdm



# column_names = ['offer_name', 'company_name', 'company_size', 'online_recruitment', 'seniority',
# 				'salary_1', 'salary_2', 'job_location', 'description', 'must_have', 'nice_to_have',
# 				# Work methodology
# 				'knowledge_repository', 'version_control_system', 'agile_management'
# 				'distributed_team', 'research_and_experimentation', 'issue_tracking_tool',

# 				# Job profile
# 				'new_features', 'maintenance', 'client_support', 'document_writing',
# 				# Equipment supplied
# 				'operating_system', 'computer', 'monitors',
# 				# Specs
# 				'start', 'contract_duration', 'paid_holiday', 'part_time_work', 'remote_possible', 
# 				'flexible_hours', 'travel_involved', 'freedom_to_choose_tools', 'job_profile'

# 				'perks_in_the_office', 'benefits']




def save_to_html(data):
	f = open('drop.html', 'w+')
	f.writelines(data)
		# must_have
		# must_have_xpath = '//nfj-postings-list[@style!="min-height:0px;"]/div/h1/a/@href'
		# must_have_xpath = '//nfj-posting-requirements[@aria-describedby="tooltip-25"]//text()'

def get_offer(url):
	# url = 'https://nofluffjobs.com/job/data-engineer-wikipedia-objectstyle-warszawa-gyghqyga'
	try:
		html = request.urlopen(url)
		sel = Selector(text=html.read(), type="html")
	except:
		print(url)

	try:
		must_have_xpath = '//nfj-posting-requirements//h3[text()="Must have"]//parent::*//text()'
		must_have = [item.strip() for item in sel.xpath(must_have_xpath).getall()[1:]]
	except:
		# print('must_have')
		must_have = None

	try:
		nice_to_have_xpath = '//nfj-posting-requirements//h3[text()="Nice to have"]//parent::*//text()'
		nice_to_have = [item.strip() for item in sel.xpath(nice_to_have_xpath).getall()[1:]]
	except:
		# print('nice_to_have')
		nice_to_have = None

	try:
		work_methodology_xpath = '//nfj-posting-methodologies//div[@class="col-sm-6 d-flex align-items-center"]//text()'
		work_methodology = [item.strip() for item in sel.xpath(work_methodology_xpath).getall()]
	except:
		# print('work_methodology')
		work_methodology = None

	try:
		equipment_supplied_xpath = '//nfj-posting-benefits//div[1]//text()'
		equipment_supplied = [item.strip() for item in sel.xpath(equipment_supplied_xpath).getall()]
	except:
		# print('equipment_supplied')
		equipment_supplied = None

	try:
		specs_xpath = '//nfj-posting-specs//div//div[1]//text()'
		specs = [item.strip() for item in sel.xpath(specs_xpath).getall()]
	except:
		# print('specs')
		specs = None

	try:
		perks_in_the_office_xpath = '//nfj-posting-perks//h3[text()="Perks in the office"]//parent::*//text()'
		perks_in_the_office = [item.strip() for item in sel.xpath(perks_in_the_office_xpath).getall()[1:]]
	except:
		# print('perks_in_the_office')
		perks_in_the_office = None

	try:
		benefits_xpath = '//nfj-posting-perks//h3[text()="Benefits"]//parent::*//text()'
		benefits = [item.strip() for item in sel.xpath(benefits_xpath).getall()[1:]]
	except:
		# print('benefits')
		benefits = None
		pass


	offer = {'must_have': must_have, 'nice_to_have': nice_to_have, 'work_methodology': work_methodology, 
				'equipment_supplied': equipment_supplied, 'specs': specs, 'perks_in_the_office': perks_in_the_office, 
				'benefits': benefits, 'url': url}
	return offer
	
	


	# xpath = '//nfj-posting-perks//h3[text()="Perks in the office"]//parent::*//text()'
	# output =sel.xpath(xpath).getall()
	# print(len(output))
	# print(output)
column_names = ['must_have', 'nice_to_have', 'work_methodology', 
				'equipment_supplied', 'specs', 'perks_in_the_office', 
				'benefits', 'url']
offers_df = pd.DataFrame(columns = column_names)

# urls=['https://nofluffjobs.com/job/cloud-infrastructure-engineer-hn-global-business-services-center-krakow-krakow-4cenlxct',
# 	   'https://nofluffjobs.com/job/mid-sr-java-developer-harvey-nash-technology-warszawa-lyfbpucr']

with open('offers_url.txt', 'r') as f:
	urls = [url.replace('\n', '') for url in f.readlines()]

# print(urls)


for url in tqdm(urls):
	# offer = get_offer()

	offers_df = offers_df.append(get_offer(url), ignore_index = True)
	time.sleep(2)


# print(offers_df)
offers_df.to_csv('text.csv', mode='w', header=True, sep=';')
