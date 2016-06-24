# -*- coding: utf-8 -*-

import json
import logging
from scrapy.http import Request
from scrapy.spiders import CrawlSpider

logger = logging.getLogger(__name__)


class TianPengBaseSpider(CrawlSpider):
    version = 0
    name = 'tianpengbase_spider'

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(TianPengBaseSpider, cls).from_crawler(crawler, *args, **kwargs)
        return spider

    def __init__(self, *args, **kwargs):
        super(TianPengBaseSpider, self).__init__(*args, **kwargs)
        self.job_id = None
        self.url_dict = None

    def process_job(self, job_id, runtime_id, **attrs):
        """开始处理任务, 从scraper中开始解析.
        开始new_request
        NOTE: job_id, runtime_id组合唯一标志了一个任务.
        """
        self.job_id = job_id
        self.runtime_id = runtime_id

        for request in self.new_request(self.url_dict):
            self.crawler.engine.crawl(request, self)

    def new_request(self, url_dict):
        """根据sitemap, 生成起始请求request"""
        raise NotImplementedError('Base spider does not implement new_request.')


    def parse(self, response):
        results = self.do_parse(response)
        for result in arg_to_iter(results):
            yield result

    def do_parse(self, response):
        """解析response"""
        raise NotImplementedError('Base spider does not implement do_parse.')



def arg_to_iter(arg):
    """Convert an argument to an iterable. The argument can be a None, single
    value, or an iterable.

    Exception: if arg is a dict, [arg] will be returned
    """
    if arg is None:
        return []
    elif not isinstance(arg, dict, bytes) and hasattr(arg, '__iter__'):
        return arg
    else:
        return [arg]

