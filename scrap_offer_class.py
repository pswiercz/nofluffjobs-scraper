import scrapy
from scrapy import Selector
from urllib import request
import pandas as pd
import time
from tqdm import tqdm
from offer_class_fields import Offer

# class Offer(scrapy.Item):
#     url = scrapy.Field()
#     offer_name = scrapy.Field()

class OfferListsSpider(scrapy.Spider):
    name = '_lists'


    def parse(self, response):
        o = Offer()

        url_xpath = ''
        offer_name_xpath = '//nfj-posting-header/div/div/h1/text()'
        company_xpath = '//nfj-posting-header//dt[text()="Company:"]//parent::*/dd/text()'
        company_size_xpath = '//nfj-posting-header//dt[text()="Company size:"]//parent::*/dd/text()'
        job_locationsalary_1_xpath = ''
        salary_1_xpath = ''
        salary_1_description_xpath = ''
        salary_2_xpath = ''
        salary_2_description_xpath = ''
        seniority_1_xpath = ''
        seniority_2_xpath = ''
        job_description_xpath = ''

        o['offer_name'] = response.xpath(offer_name_xpath).getall()[0]
        o['company'] = response.xpath(company_xpath).getall()[0].strip()
        o['company_size'] = response.xpath(company_size_xpath).getall()[0].strip()

        yield o

    
ins = OfferListsSpider()

url = 'https://nofluffjobs.com/job/remote-or-office-devops-engineer-semantive-ivdnfxnu'
html = request.urlopen(url)
sel = scrapy.Selector(text=html.read(), type="html")

gen = ins.parse(sel)

print(next(gen))



# for i in gen:
#     print(i)


# print(next(gen))


# def scrap_offer(url):
#     # url = 'https://nofluffjobs.com/'
#     html = request.urlopen(url)
#     sel = Selector(text=html.read(), type="html")
#     xpath = '//nfj-posting-seniority/div/div//div/@class'

#     drop = sel.xpath(xpath).getall()

#     print(drop)


# url = 'https://nofluffjobs.com/job/remote-or-office-devops-engineer-semantive-ivdnfxnu'

# scrap_offer(url)