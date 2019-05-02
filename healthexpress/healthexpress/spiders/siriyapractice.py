# -*- coding: utf-8 -*-
import scrapy


class SiriyapracticeSpider(scrapy.Spider):
	name = 'siriyapractice'
	allowed_domains = ['quotes.toscrape.com']
	start_urls = ["http://quotes.toscrape.com/login"]

	def parse(self, response):
		pass
