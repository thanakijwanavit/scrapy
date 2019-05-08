# -*- coding: utf-8 -*-
import scrapy
from loginform import fill_login_form


class QuotesSpider(scrapy.Spider):
    name = 'sriya'
    allowed_domains = ['119.46.164.56:8082']
    start_urls = ['http://119.46.164.56:8082/WebFront/Home/Login.aspx']
    longin_url= 'http://119.46.164.56:8082/WebFront/Home/Login.aspx'
    login_user='hx001'
    login_password='12345'

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
        quote=response.body.decode(response.encoding)
        with open('sriya.txt','w') as f:
            f.write(quote+'\n')
