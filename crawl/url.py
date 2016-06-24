# -*- coding: utf-8 -*-
import json

from format import format_config


class LoginInfoError(Exception):
    pass


class UrlSitemap(object):
    def __init__(self):
        self.start_url = None
        self.request_page_type = None
        self.actions = None
        self.keyword = None
        self.set_default_attributes()
        # self.verify()  # 校验sitemap信息正确性

    def set_default_attributes(self):
        default_settings = {
            "job_id": "",
            "runtime_id": "",
            "startUrl": "",
            "requestPageType": {
                "requestType": "Request",
                "contentType": "HTML",
                "method": "GET",
                "renderJs": False,
                "formData": {"kw":"dsgs"},
                "postKeyword":["kw"],
                "dontFilter": True,
                "headers":{}

            },
            "keyword": "",
            "actions": [],
        }
        self.set_attributes(default_settings)

    def set_attributes(self, sitemap_str):
        # 1, 如果sitemap_str是string, 则loads, 否则保持
        if isinstance(sitemap_str, (str, unicode)):
            sm_object = json.loads(sitemap_str)  # 可能会抛出ValueError
        else:
            sm_object = sitemap_str

        # 2, 格式化配置, 即将驼峰式的写法改成python式的, 并处理个别配置
        sm_object = format_config(sm_object)

        # 3, 生成sitemap对象, 如果sitemap中有sm_object中的key字段, 则覆盖sitemap变量
        for key, value in sm_object.items():
            if hasattr(self, key):
                if value is not None:
                    setattr(self, key, value)

    def find_selector(self, selector_id):
        return self.selectors.find(selector_id)

    @classmethod
    def url_sitemap_deal(cls, sitemap_str, **kwargs):
        """对传入的sitemap_str构建一个sitemap对象, 应与spider充分解耦
        :param sitemap_str: 为string或dict对象
        :return: 返回一个根据sitemap_str构建好的sitemap对象
        """
        url_sitemap = cls()
        url_sitemap.set_attributes(sitemap_str)
        # url_sitemap.start_url = get_start_url(sitemap.start_url, url_sitemap.keyword,
        #                                       **kwargs)  # 如果存在keyword不为None并且start_url符合格式那么对关键词进行处理
        # url_sitemap.request_page_type = get_request_page_type(url_sitemap.request_page_type,
        #                                                       **kwargs)  # 对post中的request_peage_type进行post关键字的处理
        # url_sitemap.after_build_sitemap()  # 当sitemap建立好之后需要处理的操作
        return url_sitemap

    def after_build_sitemap(self):
        def recusive(root):
            root.after_build_sitemap()
            for children in root.children:
                recusive(children)

        recusive(self.selectors)

    # def verify(self):
    #     checkout_login(self.login)


def checkout_login(login):
    if not login:
        return
    if not login.get('url'):
        raise LoginInfoError('login url is null.')
    if not (login.get('user_css_path') and login.get('passwd_css_path')):
        raise LoginInfoError('user_css_path or passwd_css_path is null.')
    if not (login.get('user_name') and login.get('passwd')):
        raise LoginInfoError('user_name or passwd is null.')
    if not (login.get('click_css_path')):
        raise LoginInfoError('click_css_path is null.')


if __name__ == '__main__':
    url_dict = {"dyStartUrl": {"urlTemplate": ""}, "cookies": "", "urlMatches": [], "kwds": [], "requestPageType": {"contentType": "HTML", "renderJs": False, "keyword": "kw", "requestType": "Request", "formData": {"kw": "\u4e2d\u56fd"}, "headers": {"Cookie": {"RSOUT": "lzXzXDzL1NbmrGWwvQdvjdL1hyMDQKV4Tn2wJgXT3NTssy4r9TTl!121744264", "BIGipServerpool_zdw_www": "w8U/sz7NcG9C2u5kmji0x1PtwZ1aGOjPAwJ1qlnGCiujUcoXXnOP+FalTBmHukIDzDuvP7/xk9aFfA==", "BIGipServerpool_rs": "INyjUsil6qKm+/HBYrRM2gawWIhYTqJIwMtgtaJvP8MILjP1eB/D7928w53YS+wfxjeHJRL6K4AdVis=", "JSESSIONID": "A362200AC4CAE3BBBC2585C743147D7F"}, "Referer": "http://www.zhongdengwang.org.cn/zhongdeng/index.shtml", "Accept-Encoding": "gzip, deflate", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}, "method": "post"}, "schedulerType": "interval", "actions": [], "selectors": [{"currentUrl": "http://www.zhongdengwang.org.cn/search/WebsiteSearch.jsp", "multiple": True, "parentSelectors": ["_root"], "selector": "div.search_con.search_con1", "iframeUrl": "", "scrollTop": "268", "type": "SelectorElement", "id": "items", "selectorName": ""}, {"currentUrl": "http://www.zhongdengwang.org.cn/search/WebsiteSearch.jsp", "multiple": False, "parentSelectors": ["items"], "selector": "a", "iframeUrl": "", "scrollTop": "225", "type": "SelectorText", "id": "title", "selectorName": ""}, {"currentUrl": "http://www.zhongdengwang.org.cn/search/WebsiteSearch.jsp", "multiple": False, "parentSelectors": ["items"], "selector": "a", "typename": "\u94fe\u63a5\u578b(Link)", "iframeUrl": "", "scrollTop": "225", "type": "SelectorLink", "id": "link", "selectorName": ""}, {"currentUrl": "http://www.zhongdengwang.org.cn/search/WebsiteSearch.jsp", "multiple": False, "parentSelectors": ["items"], "selector": "div.search_con_tit span", "iframeUrl": "", "scrollTop": "225", "type": "SelectorText", "id": "time", "selectorName": ""}], "versionName": "\u7cbe\u51c6\u6269\u5c55", "childnum": 4, "version": 1, "scheduler": {"status": 0}, "login": {}, "_id": "zhongdeng_test", "latestEdition": "20160524105824", "startUrl": "http://www.zhongdengwang.org.cn/search/WebsiteSearch.jsp"}
    UrlSitemap.url_sitemap_deal(url_dict)
