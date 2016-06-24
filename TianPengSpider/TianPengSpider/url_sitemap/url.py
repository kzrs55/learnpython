# -*- coding: utf-8 -*-

class UrlSitemap(object):
    def __init__(self,start_url=None,request_page_type=None,actions=None,keyword=None):
        self.start_url = start_url
        self.request_page_type = request_page_type
        self.actions = actions
        self.keyword = keyword
        # self.verify()  # 校验sitemap信息正确性


if __name__ == '__main__':
    url_dict = {"dyStartUrl": {"urlTemplate": ""}, "cookies": "", "urlMatches": [], "kwds": [], "requestPageType": {"contentType": "HTML", "renderJs": False, "keyword": "kw", "requestType": "Request", "formData": {"kw": "\u4e2d\u56fd"}, "headers": {"Cookie": {"RSOUT": "lzXzXDzL1NbmrGWwvQdvjdL1hyMDQKV4Tn2wJgXT3NTssy4r9TTl!121744264", "BIGipServerpool_zdw_www": "w8U/sz7NcG9C2u5kmji0x1PtwZ1aGOjPAwJ1qlnGCiujUcoXXnOP+FalTBmHukIDzDuvP7/xk9aFfA==", "BIGipServerpool_rs": "INyjUsil6qKm+/HBYrRM2gawWIhYTqJIwMtgtaJvP8MILjP1eB/D7928w53YS+wfxjeHJRL6K4AdVis=", "JSESSIONID": "A362200AC4CAE3BBBC2585C743147D7F"}, "Referer": "http://www.zhongdengwang.org.cn/zhongdeng/index.shtml", "Accept-Encoding": "gzip, deflate", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}, "method": "post"}, "schedulerType": "interval", "actions": [], "selectors": [{"currentUrl": "http://www.zhongdengwang.org.cn/search/WebsiteSearch.jsp", "multiple": True, "parentSelectors": ["_root"], "selector": "div.search_con.search_con1", "iframeUrl": "", "scrollTop": "268", "type": "SelectorElement", "id": "items", "selectorName": ""}, {"currentUrl": "http://www.zhongdengwang.org.cn/search/WebsiteSearch.jsp", "multiple": False, "parentSelectors": ["items"], "selector": "a", "iframeUrl": "", "scrollTop": "225", "type": "SelectorText", "id": "title", "selectorName": ""}, {"currentUrl": "http://www.zhongdengwang.org.cn/search/WebsiteSearch.jsp", "multiple": False, "parentSelectors": ["items"], "selector": "a", "typename": "\u94fe\u63a5\u578b(Link)", "iframeUrl": "", "scrollTop": "225", "type": "SelectorLink", "id": "link", "selectorName": ""}, {"currentUrl": "http://www.zhongdengwang.org.cn/search/WebsiteSearch.jsp", "multiple": False, "parentSelectors": ["items"], "selector": "div.search_con_tit span", "iframeUrl": "", "scrollTop": "225", "type": "SelectorText", "id": "time", "selectorName": ""}], "versionName": "\u7cbe\u51c6\u6269\u5c55", "childnum": 4, "version": 1, "scheduler": {"status": 0}, "login": {}, "_id": "zhongdeng_test", "latestEdition": "20160524105824", "startUrl": "http://www.zhongdengwang.org.cn/search/WebsiteSearch.jsp"}
    start_url = [url_dict.get("startUrl")]
    request_page_type = url_dict.get("requestPageType")
    actions = url_dict.get("actions")


    # actions =
