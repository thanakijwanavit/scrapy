# -*- coding: utf-8 -*-
import json
import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser

class SiriyapracticeSpider(scrapy.Spider):
        name = 'siriyapractice'
        allowed_domains = ['119.46.164.56:8082']
        start_urls = ["http://119.46.164.56:8082/WebFront/Home/Login.aspx"]

        def scrape_pages(self,response):
            with open('scraped_page.html','w') as f:
                f.write(response.body.decode(response.encoding))
            open_in_browser(response)
        def parse(self, response):
            __VIEWSTATE = response.xpath('//*[@name="__VIEWSTATE"]/@value').extract_first()
            __VIEWSTATEGENERATOR = response.xpath('//*[@name="__VIEWSTATEGENERATOR"]/@value').extract_first()
            __EVENTVALIDATION = response.xpath('//*[@name="__EVENTVALIDATION"]/@value').extract_first()
            formdata={
            '__EVENTTARGET':'cBtnLogin',
            '__EVENTARGUMENT': '',
            '__VIEWSTATE':__VIEWSTATE,
            '__VIEWSTATEGENERATOR':__VIEWSTATEGENERATOR,
            '__EVENTVALIDATION':__EVENTVALIDATION,
            'cTxUserName':'hx001',
            'cTxPassword':'12345',
            'cHdComputerName': '',
            'cHdComputerIP':'124.122.127.218',
            'cHdIsUpdateComDetComplete':'false'
                                        }
            with open('output.txt','w') as f:
                f.write(json.dumpa(formdata))
            return FormRequest.from_response(response,
                                    formdata=formdata,
                                    callback=self.scrape_pages)

