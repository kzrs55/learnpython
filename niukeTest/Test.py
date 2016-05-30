#coding=utf-8
from pip._vendor.distlib.compat import raw_input

__author__ = 'zjutK'
start_url={ "params": {"p":u"杭州"},"urlTemplate": "http://www.court.gov.cn/search.html?content={p}"}

for i,j in start_url.items():
    print(i,)