#coding=utf-8
__author__ = 'zjutK'
'''
'16/4/27下午8:39'

'''
import urllib

import sgmllib



class handle_html(sgmllib.SGMLParser):

       #unknown_starttag这个方法在任意的标签开始被解析时调用

       #tag为标签名

       #attrs表示标签的参赛

   def unknown_starttag(self, tag, attrs):

       print "-------"+tag+" start--------"

       print attrs

       #unknown_endtag这个方法在任意标签结束被解析时被调用

   def unknown_endtag(self, tag):

       print "-------"+tag+" end----------"



web =urllib.urlopen("http://freebuf.com/")

web_handler = handle_html()

#数据传入解析器

web_handler.feed(web.read())