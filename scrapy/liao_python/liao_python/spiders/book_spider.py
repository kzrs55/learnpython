# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from liao_python.items import LiaoPythonItem


class BookSpider(CrawlSpider):
    name = "bookspider"
    allowed_domains = ['liaoxuefeng.com']
    start_urls = ['http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000']
    rules = (Rule(LinkExtractor(allow=("001374738125095c955c1e6d8bb493182103fac9270762a000/\w+"))),)
    def parse(self, response):
        item = LiaoPythonItem()
        item['content'] = response.xpath('//*[@id="main"]/div[3]/div[2]/div/div[2]/div[2]/div[2]/text()').extract()
        item['title'] = response.xpath('//*[@id="main"]/div[3]/div[2]/div/div[2]/div[2]/h4/text()').extract()
        return item
