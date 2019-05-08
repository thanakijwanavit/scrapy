# -*- coding: utf-8 -*-
import scrapy


class ChemicalsSpider(scrapy.Spider):
    name = 'chemicals'
    allowed_domains = ['www.scgchemicals.com']
    start_urls = ['https://www.scgchemicals.com/en/sitemap#']

    def parse(self, response):
        return scrapy
