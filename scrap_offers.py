import scrapy
from scrapy import Selector
from urllib import request
import pandas as pd
from os import listdir

import datetime
import time
from datetime import date

from tqdm import tqdm
from column_names import column_names


from class_items import Offer
from xpath_list import *
 
MAX_100_PAGES = False

class OfferListsSpider(scrapy.Spider):
    name = '_lists'
    def __init__(self):
        t = time.localtime()
        self.file_name = f"offers//offers_{date.today()}_{time.strftime('%H-%M-%S', t)}.csv"
        pd.DataFrame(columns = column_names).to_csv(self.file_name, mode='w', header=True, sep=';')
        self.df_index = 0

    def get_offer(self, url):
        html = request.urlopen(url)
        sel = scrapy.Selector(text=html.read(), type="html")
        gen = self.parse(sel)

        self.offer_data = dict(next(gen))

        for key, item in self.offer_data.items():
            if item:
                if '\r' in item:
                    item = ''.join(item.splitlines())
                self.offer_data[key] = item.lstrip().rstrip()

        self.offer_data['url'] = url

        print(self.offer_data)

        self.offers_df = pd.DataFrame(columns = column_names)
        self.offers_df = self.offers_df.append(self.offer_data, ignore_index=True)
        self.offers_df.index = [self.df_index]
        self.df_index += 1

        self.offers_df.to_csv(self.file_name, mode='a', header=False, sep=';')

    def parse(self, response):
        o = Offer()

        o['offer_name'] = response.xpath(offer_name_xpath).get()
        o['company'] = response.xpath(company_xpath).get()
        o['company_size'] = response.xpath(company_size_xpath).get()
 
        job_location = []  
        for item in response.xpath(job_location_xpath).getall():
            job_location += item.split(', ')
            job_location = [item.lstrip().rstrip() for item in job_location]

        o['job_location'] = ', '.join(job_location) 

        o['salary_1'] = response.xpath(salary_1_xpath).get()
        o['salary_1_description'] = response.xpath(salary_1_description_xpath).get()
        o['salary_2'] = response.xpath(salary_2_xpath).get()
        o['salary_2_description'] = response.xpath(salary_2_description_xpath).get()
        o['salary_bonus'] = response.xpath(salary_bonus_xpath).get()                
        o['seniority_1'] = response.xpath(seniority_1_xpath).get()
        o['seniority_2'] = response.xpath(seniority_2_xpath).get()
        o['job_description'] = response.xpath(job_description_xpath).get()

        o['must_have'] = ', '.join([item.strip() for item in response.xpath(must_have_xpath).getall()])
        o['nice_to_have'] = ', '.join([item.strip() for item in response.xpath(nice_to_have_xpath).getall()])

        ## work_methodology_category
        o['integration_tests'] = response.xpath(integration_tests_xpath).get()
        o['unit_tests'] = response.xpath(unit_tests_xpath).get()
        o['tester'] = response.xpath(tester_xpath).get()
        o['agile_management'] = response.xpath(agile_management_xpath).get()
        o['issue_tracking_tool'] = response.xpath(issue_tracking_tool_xpath).get()
        o['knowledge_repository'] = response.xpath(knowledge_repository_xpath).get()
        o['code_reviews'] = response.xpath(code_reviews_xpath).get()
        o['static_code_analysis'] = response.xpath(static_code_analysis_xpath).get()
        o['version_control_system'] = response.xpath(version_control_system_xpath).get()
        o['build_server'] = response.xpath(build_server_xpath).get()
        o['qa_manager'] = response.xpath(qa_manager_xpath).get()
        o['distributed_team'] = response.xpath(distributed_team_xpath).get()
        o['research_and_experimentation'] = response.xpath(research_and_experimentation_xpath).get()
        o['pair_programming'] = response.xpath(pair_programming_xpath).get()
        o['workshops'] = response.xpath(workshops_xpath).get()
        o['e2e_tests'] = response.xpath(e2e_tests_xpath).get()
        o['commit_on_the_first_day'] = response.xpath(commit_on_the_first_day_xpath).get()
        o['one_command_build_possible'] = response.xpath(one_command_build_possible_xpath).get()
        o['up_and_running_within_2h'] = response.xpath(up_and_running_within_2h_xpath).get()
        o['high_level_and_low_level_designs'] = response.xpath(high_level_and_low_level_designs_xpath).get()
        o['feature_development_and_porting'] = response.xpath(feature_development_and_porting_xpath).get()
        o['regression_testing'] = response.xpath(regression_testing_xpath).get()
        o['uat_testing'] = response.xpath(uat_testing_xpath).get()
        o['agile_testing'] = response.xpath(agile_testing_xpath).get()
        o['manual_tests'] = response.xpath(manual_tests_xpath).get()
        o['database'] = response.xpath(database_xpath).get()
        o['virtualization'] = response.xpath(virtualization_xpath).get()
        o['cloud_infrastructure'] = response.xpath(cloud_infrastructure_xpath).get()
        o['databases'] = response.xpath(databases_xpath).get()
        o['network_virtualization'] = response.xpath(network_virtualization_xpath).get()
        o['provisioning'] = response.xpath(provisioning_xpath).get()
        o['networking_hardware'] = response.xpath(networking_hardware_xpath).get()
        o['security'] = response.xpath(security_xpath).get()
        o['application_stack'] = response.xpath(application_stack_xpath).get()

        ## Equipment supplied
        operating_system_1 = response.xpath(operating_system_1_xpath).getall()
        operating_system_2 = response.xpath(operating_system_2_xpath).getall()
        system = str()
        for i, active in enumerate(operating_system_1):
            if active:
                _, system_temp = operating_system_2[i].split('#')
                if system:
                    system += ', ' + system_temp 
                else:
                    system += system_temp 
        o['operating_system'] = system
        o['computer'] = response.xpath(computer_xpath).get()
        o['monitors'] = response.xpath(monitors_xpath).get()

        ## specs_category
        o['job_profile'] = response.xpath(job_profile_xpath).get()
        o['start'] = response.xpath(start_xpath).get()
        o['contract_duration'] = response.xpath(contract_duration_xpath).get()
        o['paid_holiday'] = response.xpath(paid_holiday_xpath).get()
        o['part_time_work'] = response.xpath(part_time_work_xpath).get()
        o['remote_possible'] = response.xpath(remote_possible_xpath).get()
        o['flexible_hours'] = response.xpath(flexible_hours_xpath).get()
        o['travel_involved'] = response.xpath(travel_involved_xpath).get()
        o['freedom_to_choose_tools'] = response.xpath(freedom_to_choose_tools_xpath).get()
        o['relocation_package'] = response.xpath(relocation_package_xpath).get()
        o['remote_work'] = response.xpath(remote_work_xpath).get()
        o['open_minded_developers_in_team'] = response.xpath(open_minded_developers_in_team_xpath).get()
        o['work_with_international_client'] = response.xpath(work_with_international_client_xpath).get()

        o['perks_in_the_office'] = ', '.join([item.strip() for item in response.xpath(perks_in_the_office_xpath).getall()[1:]])
        o['benefits'] = ', '.join([item.strip() for item in response.xpath(benefits_xpath).getall()[1:]])

        yield o

def get_urls(file_to_get = 'urls_sec_2020-04-20_21-39-55.txt'):
    try:
        with open(f'urls/{file_to_get}', 'r') as f:
            urls = [url.replace('\n', '') for url in f.readlines()]
        return urls
    except:
        print('given file with urls does not exist')

if __name__ == '__main__':
    # print(get_urls())
    urls = get_urls()

    if urls:
        ins = OfferListsSpider()    
        for i, url in enumerate(tqdm(urls)):
            if i >= 100 and MAX_100_PAGES:
                break

            ins.get_offer(url)
            time.sleep(2)








    # onlyfiles = [f for f in listdir(.) if isfile(join(mypath, f))]
    # print(onlyfiles)

    # with open('urls/1', 'r') as f:
    #     print(f.readlines())

    # url = 'https://nofluffjobs.com/job/frontend-developer-mindbox-krakow-re0eq0hd' # 2 salary
    # url2 = 'https://nofluffjobs.com/job/software-engineer-privitar-warsaw-rnssdlbi' 
    # ins = OfferListsSpider()
    # ins.get_offer(url2)
    # time.sleep(1)


 # if which_to_get == 'Newest':

    #     date_list = []
    #     time_list = []
    #     # listdir('./urls')
    #     url = listdir('./urls')[0]

    #     *_, date, time = url.split('_') 
    #     date_list.append(date)
    #     time_list.append(time[:-4])

    #     print(date_list, time_list)

    #     sorted(data,
    #    key=lambda each_dict: (datetime.strptime(each_dict['date'], '%d-%b-%Y'),
    #                           datetime.strptime(each_dict['time'], '%H:%M:%S.%f'))