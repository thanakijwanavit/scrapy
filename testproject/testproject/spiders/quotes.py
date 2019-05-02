# -*- coding: utf-8 -*-
import scrapy
from loginform import fill_login_form


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com//']
    longin_url= 'http://quotes.toscrape.com/login'
    login_user='fdasfa'
    login_password='sdaffad'

    def init_request(self):
        return scrapy.Request(
            url=self.login_url,
            callback=self.login,
            )
    def login(self,response):
        data,url,method = fill_login_form(response.url,response.body,self.login_user,self.login_password)
        return scrapy.FormRequest(url,formdata=dict(data),
                                method=method, callback=self.parse)
    def parse(self, response):
       quotes= response.xpath("//div[@class='quote']//span[@class='text']/text()").extract()
       with open('quotes.txt','w') as f:
           for quote in quotes:
               f.write(quote+'\n')
       yield {'quotes':quotes}
