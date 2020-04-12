from scrapy import Selector
from urllib import request
import pandas as pd
import time
from tqdm import tqdm


work_methodology_category = ['Integration tests', 'Unit tests', 'Tester', 'Agile management', 'Issue tracking tool', 
'Knowledge repository', 'Code reviews', 'Static code analysis', 'Version control system', 
'Build server', 'QA manager', 'Distributed team', 'Research and Experimentation', 'Pair programming', 
'Workshops', 'e2e tests', 'Commit on the first day', 'One command build possible', 'Up and running within 2h', 
'High level and low level designs', 'Feature development and porting', 'Regression testing', 
'UAT testing', 'Agile Testing', 'Manual tests', 'Database', 'Virtualization', 'Cloud infrastructure', 
'Operating system', 'Databases', 'Network virtualization', 'Provisioning', 'Networking hardware', 'Security', 
'Application stack', 'Operating systems']

equipment_supplied_category = ['Operating System', 'Computer', 'Monitors']

specs_category = ['Job profile', 'Start', 'Contract duration', 'Paid holiday', 'Part time work', 'Remote possible',
'Flexible hours', 'Travel involved', 'Freedom to choose tools', 'Relocation package', 'Remote work', 
'Open-minded developers in team', 'Work with international client']

columns = ['date of scrap', 'url', 'offer name', 'company', 'company size', 'job location'
'salary 1', 'salary 1 description', 'salary 2', 'salary 2 description',
'seniority 1', 'seniority 2', 'job description', 'Must have', 'Nice to have',
*work_methodology_category, *equipment_supplied_category, *specs_category,

'Perks in the office', 'Benefits']

print(len(columns))
print(columns)


def scrap_offer(url):
	# url = 'https://nofluffjobs.com/'
	html = request.urlopen(url)
	sel = Selector(text=html.read(), type="html")
	xpath = '//nfj-posting-seniority/div/div//div/@class'

	drop = sel.xpath(xpath).getall()

	

# url = 'https://nofluffjobs.com/job/remote-or-office-devops-engineer-semantive-ivdnfxnu'


 



