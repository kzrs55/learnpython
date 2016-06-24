# -*- coding: utf-8 -*-

# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.


from scrapy import Request, FormRequest
from scrapy.spiders import CrawlSpider


class TianPengSpider(CrawlSpider):
    version = 0
    name = 'tianpeng_spider'

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        return super(TianPengSpider, cls).from_crawler(crawler, *args, **kwargs)

    def new_request(self, url_dict):
        """起始请求.
            1, 从url_dict中获取url的request_page_type,actions
            2, 将start_url生成初始请求
        """
        request_page_type = url_dict.get("requestPageType")  # for the start_url
        actions = url_dict.get('actions')
        for url in url_dict.start_url:
            request = self.gen_request(url, request_page_type, actions=actions, is_pagination=True)
            yield request

    def gen_request(self, url, request_page_type, login=None, parent_selector=None, is_pagination=False,
                    dont_filter=False, actions=None):
        """根据meta信息生成请求对象.
        :param url: Request对象所对应的url地址
        :param request_page_type: 以怎么样的方式访问该url地址
        :param is_pagination: 是否为分页请求
        :return: 根据上述的字段返回请求
        """
        rqt = request_page_type.copy()
        request_type = rqt.get('request_type', 'Request')
        method = rqt.get('method', 'GET')
        headers = rqt.get('headers') or rqt.get('Headers')
        form_data = rqt.get('form_data')
        _dont_filter = dont_filter if dont_filter else rqt.get('dont_filter')  # the url filter or not.

        meta = {
            'request_page_type': rqt,
            'job_id': self.job_id,
            'runtime_id': self.runtime_id,
            "actions": actions,
        }

        if request_type.startswith('R'):
            cookie = headers.get('Cookie') if headers else None
            return Request(url, callback=self.parse, method=method, cookies=cookie,
                           meta=meta)
        else:
            return FormRequest(url, callback=self.parse, method=method, formdata=form_data,
                               dont_filter=_dont_filter, meta=meta)

    def do_parse(self, response):
        """返回response
        """
        # encode_format = chardet.detect(response.body)
        # response = response.replace(body=response.body.decode(encode_format['encoding']), encoding='utf-8')
        yield response