#coding=utf-8
import html

__author__ = 'zjutK'

def make_element(name,value,**attrs):
    keyvals=['%s="%s"'% item for item in attrs.items()]
    attr_str=''.join(keyvals)
    element='<{name}{attrs}>{value}</{name}>'.format(
        name=name,
        attrs=attr_str,
        value=html.escape(value)
    )
    print(element)


make_element('item','kent',size='large',quantity=6)