# -*- coding: utf-8 -*-

import os
import logging
from scrapy.exceptions import DontCloseSpider
from scrapy import signals
from scrapy.spiders import Spider

logger = logging.getLogger(__name__)


class AutoSeed(object):
    """该Scrapy扩展用于在Spider发出idle信号时, 主动去ZooKeeper上获取一个任务
    然后raise一个DontCloseSpider异常告诉Scrapy不要关闭爬虫.

    该爬虫持有封装过的ZooKeeper客户端交流的对象, Scrapy与ZooKeeper的交流都通过该对象
    """

    def __init__(self, crawler):
        self.crawler = crawler
        self.first_request_test_job = True      # 仅用于测试

    @classmethod
    def from_crawler(cls, crawler):
        o = cls(crawler)
        crawler.signals.connect(o.spider_idle, signal=signals.spider_idle)
        crawler.signals.connect(o.spider_opened, signal=signals.spider_opened)
        return o

    def spider_opened(self, spider):
        """当spider open时候, 生成ZooKeeper客户端对象, 并注册该spider"""
        settings = spider.crawler.settings
        self.register_spider(spider)
        logger.info('ZZZ Registered spider-%(name)s on ZooKeeper.', {'name': spider.name})

    def spider_idle(self, spider):
        """当spider收到idle信号时, 去ZooKeeper上获取一个任务, 再抛出DontCloseSpider异常"""
        self.request_new_job(spider)
        raise DontCloseSpider()

    def request_new_job(self, spider):
        if os.environ.get('TEST') == 'True':
            if self.first_request_test_job is False:
                return
            self.first_request_test_job = False
            test_job = self.request_test_job(spider)
            logger.info('ZZZ Get Test Job-%(id)s, RuntimeId-%(runtime_id)s from Local.',
                        {'id': test_job.job_id, 'runtime_id': test_job.runtime_id})
            spider.process_job(test_job.job_id, test_job.runtime_id, None)
            return

        spider_znode = self._get_spider_info(spider)

    def register_spider(self, spider):
        """生成爬虫的znode, 并注册到ZooKeeper上"""
        assert isinstance(spider, Spider), 'spider must be a instance of scrapy spider.'
        new_spider_znode = self.scheduler.register_spider(spider)
        self.spider2znode[spider] = new_spider_znode
        self.update_spider_id(spider, new_spider_znode)
        return new_spider_znode

    def update_spider_id(self, spider, new_spider_znode):
        """ 解析新注册生成的临时顺序节点的后缀编号 """
        old_id = spider.identifier
        node = new_spider_znode.real_path.split("/")[-1]
        spider.identifier = node  # 将zookeeper中生成的节点名作为spider的标识
        logger.info('ZZZ Change Spider identifier from=%(old)s To=%(new)s By ZooKeeper path=%(real_path)s......', {"old": old_id, "new": spider.identifier, "real_path": new_spider_znode.real_path})

    def request_test_job(self, spider):
        """用于测试"""
        # test_job = Job(887, "com.test_spider.www", runtime_id="8750001")
        return


