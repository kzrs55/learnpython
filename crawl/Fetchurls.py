#coding=utf-8
import threading
from urllib import request
from urllib.error import URLError

__author__ = 'zjutK'
'''
'16/4/27下午7:15'
'''

class FetchUrl(threading.Thread):
    def __init__(self,urls,output):
        super().__init__()
        self.urls=urls
        self.output=output

    def run(self):
        while self.urls:
            url=self.urls.pop()
            req=request.Request(url)
            try:
                d=request.urlopen(req)
            except URLError as e:
                print('URL %s failed: %s' % (url, e.reason))
            # print(d.read())
            self.output.write(d.read().decode('utf-8'))
            print('write done by %s' % self.name)
            print('URL %s fetched by %s' % (url, self.name))

def main():
    urls1=['http://www.baidu.com','http://www.qq.com']
    urls2=['http://www.neitui.me','http://www.sina.com']
    f=open('output.txt','w+')
    t1=FetchUrl(urls1,f)
    t2=FetchUrl(urls2,f)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    f.close()
if __name__ == '__main__':
    main()
