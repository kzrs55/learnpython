#coding=utf-8
__author__ = 'zjutK'

import re
url= 'www.baidu.com/{p}'
search_keywords={"p":1}

keywords_value_re={}

for keywords_name,keywords_value in search_keywords.items():
        search_keywords[keywords_name]=keywords_value
        keywords_value_re[keywords_name] = re.compile(r'{%s}' % keywords_name)

for
search_keywords_list=list(search_keywords)



