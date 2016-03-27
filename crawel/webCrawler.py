# -*- coding: gb2312 -*-
import ConfigParser
import cookielib
import urllib
import urllib2
import BeautifulSoup
from PIL import Image
import pytesseract
import re
import time

__author__ = 'kzrs55'
# 涉及到的各页面地址
mainurl = 'http://119.97.194.18:4503/'
hosturl = 'http://119.97.194.18:4503/Default.aspx'
imgurl = 'http://119.97.194.18:4503/ImageCode.aspx'
# 排放口1
# finalurl='http://119.97.194.18:4503/pcSingleData/LastData.aspx?StationName=%be%a3%d6%dd%ca%d0%bc%af%c3%c0%c8%c8%b5%e7%d3%d0%cf%de%d4%f0%c8%ce%b9%ab%cb%be%b7%cf%c6%f8%c5%c5%b7%c5%bf%da%a3%a31'
# 排放口2
# finalurl='http://119.97.194.18:4503/pcSingleData/LastData.aspx?StationName=%be%a3%d6%dd%ca%d0%bc%af%c3%c0%c8%c8%b5%e7%d3%d0%cf%de%d4%f0%c8%ce%b9%ab%cb%be%b7%cf%c6%f8%c5%c5%b7%c5%bf%da%a3%a32'
# last
# finalurl='http://119.97.194.18:4503/pcSingleData/LastData.aspx?StationName=%ba%fe%b1%b1%cb%c9%d4%b4%ed%b7%ca%af%b7%a2%b5%e7%d3%d0%cf%de%b9%ab%cb%be(%d7%dc%c5%c5%bf%da%d7%b0%bb%fa%c8%dd%c1%bf2.5%cd%f2%c7%a7%cd%df)'
finalurl = 'http://119.97.194.18:4503/pcSingleData/LastData.aspx'
stationname2 = '%be%a3%d6%dd%ca%d0%bc%af%c3%c0%c8%c8%b5%e7%d3%d0%cf%de%d4%f0%c8%ce%b9%ab%cb%be%b7%cf%c6%f8%c5%c5%b7%c5%bf%da%a3%a32'
stationname1 = '%be%a3%d6%dd%ca%d0%bc%af%c3%c0%c8%c8%b5%e7%d3%d0%cf%de%d4%f0%c8%ce%b9%ab%cb%be%b7%cf%c6%f8%c5%c5%b7%c5%bf%da%a3%a31'
# 生成config对象
conf = ConfigParser.ConfigParser()
# 用config对象读取配置文件
conf.read("crawler.cfg")
# 指定section，option读取值
user = conf.get("settings", "user")
password = conf.get("settings", "password")
postdata2 = urllib.urlencode({
    'StationID': 42100042100302,
    'StationName': stationname2,
    'KindID': 35,
})
postdata1 = urllib.urlencode({
    'StationID': 42100042100301,
    'StationName': stationname1,
    'KindID': 35,
})
# 初始化一个CookieJar来处理Cookie的信息#
cookie = cookielib.CookieJar()
# 创建一个新的opener来使用我们的CookieJar#
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
result = opener.open(mainurl)
for item in cookie:
    mycookie = item.name + '=' + item.value
    print "cookie=" + mycookie
loginheaders = {
    'Host': '119.97.194.18:4503',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://119.97.194.18:4503/Default.aspx',
    'Cookie': mycookie,
    'Connection': 'keep-alive',
    # 'Content-Type':'application/x-www-form-urlencoded',
    # 'Content-Length':'423'
}


def load():
    boolean = True;
    while boolean:
        request = urllib2.Request(url=imgurl, data=None, headers=loginheaders)
        response = urllib2.urlopen(request)
        myimg = "C:code.jpg"
        dlimg = open(myimg, 'wb')
        dlimg.write(response.read())
        dlimg.close()

        # 识别并输入验证码
        im = Image.open(myimg)
        mycode = pytesseract.image_to_string(im)
        # 模拟登陆页面 ，并获取登陆后返回的页面
        loginpostData = {
            '__VIEWSTATE': '/wEPDwUKLTQ5NjAyMzY4Nw8WAh4IcGFzc2NvZGUFBDk1MDdkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYBBQZjaGtSZW1y7jFce70qxCpFrAi8Zjpn3OkM82lDcMs4ttBf44VqKg==',
            # 一堆编码，暂不知道作何用
            '__EVENTVALIDATION': '/wEWBwKq+bGyAQLYzu/ODgKl1bKzCQK1qbSWCwKIwcnbDwKK+ragDQLb18frA3HdAgeoCC+HsJrGpQtloOQHmAgodvZXNlh+d+eGiI1d',
            # 又是一堆编码，暂不知道作何用
            'hidUserScreenWidth': 1920,
            'txtUserName': user,
            'txtPassWord': password,
            'txtImgCode': mycode,
            'ibtnOK': '登陆'
        }
        loginpostData = urllib.urlencode(loginpostData)
        request = urllib2.Request(hosturl, loginpostData, loginheaders)
        response = urllib2.urlopen(request)
        text = response.read()
        pattern = re.compile('荆州市集美热电有限责任公司废气')  # 通过分析获取到的页面判断是否登陆成功，应该有更简便的方法
        if pattern.findall(text):
            print "登陆成功。。。"
            boolean = False
        else:
            print "登陆失败。。。"


print "正在登录。。。"
load()
print "开始爬取数据"
while 1 > 0:
    # 荆州市集美热电有限责任公司废气排放口1
    request = urllib2.Request(url=finalurl, data=postdata1, headers=loginheaders)
    response = urllib2.urlopen(request)
    doc = response.read()
    htmlCharset = "GB2312"

    soup = BeautifulSoup.BeautifulSoup(doc, fromEncoding=htmlCharset)
    timeNow1 = soup.html.body.form.table.ul.text
    str = soup.html.body.form.table.text
    Line1 = "1#;" + timeNow1 + ';'
    if str.find('SO2(Rtd)') > 0:
        Line1 = Line1 + str.split('SO2(Rtd)')[1].split('mg/m3')[0] + ';'
    else:
        Line1 = Line1 + ';'
    if str.find('SO2(ZsRtd)') > 0:
        Line1 = Line1 + str.split('SO2(ZsRtd)')[1].split('mg/m3')[0] + ';'
    else:
        Line1 = Line1 + ';'
    if str.find('NOx(ZsRtd)') > 0:
        Line1 = Line1 + str.split('NOx(ZsRtd)')[1].split('mg/m3')[0] + ';'
    else:
        Line1 = Line1 + ';'
    if str.find('NOx(Rtd)') > 0:
        Line1 = Line1 + str.split('NOx(Rtd)')[1].split('mg/m3')[0] + ';'
    else:
        Line1 = Line1 + ';'
    if str.find(u'O2含量(Rtd)') > 0:
        Line1 = Line1 + str.split(u'O2含量(Rtd)')[1].split('%')[0] + ';'
    else:
        Line1 = Line1 + ';'
    if str.find(u'烟尘(ZsRtd)') > 0:
        Line1 = Line1 + str.split(u'烟尘(ZsRtd)')[1].split('mg/m3')[0] + ';'
    else:
        Line1 = Line1 + ';'
    if str.find(u'烟尘(Rtd)') > 0:
        Line1 = Line1 + str.split(u'烟尘(Rtd)')[1].split('mg/m3')[0] + ';'
    else:
        Line1 = Line1 + ';'
    if str.find(u'烟气流速(Rtd)') > 0:
        Line1 = Line1 + str.split(u'烟气流速(Rtd)')[1].split('m/s')[0] + ';'
    else:
        Line1 = Line1 + ';'
    if str.find(u'烟气压力(Rtd)') > 0:
        Line1 = Line1 + str.split(u'烟气压力(Rtd)')[1].split('kpa')[0] + ';'
    else:
        Line1 = Line1 + ';'
    if str.find(u'烟气温度(Rtd)') > 0:
        Line1 = Line1 + str.split(u'烟气温度(Rtd)')[1].split(u'℃')[0] + ';'
    else:
        Line1 = Line1 + ';'
    if str.find(u'废气流量(Rtd)') > 0:
        Line1 = Line1 + str.split(u'废气流量(Rtd)')[1].split('m3/s')[0] + ';'
    else:
        Line1 = Line1 + ';'
    if str.find(u'烟气湿度(Rtd)') > 0:
        Line1 = Line1 + str.split(u'烟气湿度(Rtd)')[1].split('%')[0] + ';'
    else:
        Line1 = Line1 + ';'


    # 荆州市集美热电有限责任公司废气排放口2
    request = urllib2.Request(url=finalurl, data=postdata2, headers=loginheaders)
    response = urllib2.urlopen(request)
    doc = response.read()
    htmlCharset = "GB2312"
    soup = BeautifulSoup.BeautifulSoup(doc, fromEncoding=htmlCharset)
    timeNow2 = soup.html.body.form.table.ul.text
    str = soup.html.body.form.table.text
    # str=str.encode('gbk')
    Line2 = "2#;" + timeNow2 + ';'
    if str.find('SO2(Rtd)') > 0:
        Line2 = Line2 + str.split('SO2(Rtd)')[1].split('mg/m3')[0] + ';'
    else:
        Line2 = Line2 + ';'
    if str.find('SO2(ZsRtd)') > 0:
        Line2 = Line2 + str.split('SO2(ZsRtd)')[1].split('mg/m3')[0] + ';'
    else:
        Line2 = Line2 + ';'
    if str.find('NOx(ZsRtd)') > 0:
        Line2 = Line2 + str.split('NOx(ZsRtd)')[1].split('mg/m3')[0] + ';'
    else:
        Line2 = Line2 + ';'
    if str.find('NOx(Rtd)') > 0:
        Line2 = Line2 + str.split('NOx(Rtd)')[1].split('mg/m3')[0] + ';'
    else:
        Line2 = Line2 + ';'
    if str.find(u'O2含量(Rtd)') > 0:
        Line2 = Line2 + str.split(u'O2含量(Rtd)')[1].split('%')[0] + ';'
    else:
        Line2 = Line2 + ';'
    if str.find(u'烟尘(ZsRtd)') > 0:
        Line2 = Line2 + str.split(u'烟尘(ZsRtd)')[1].split('mg/m3')[0] + ';'
    else:
        Line2 = Line2 + ';'
    if str.find(u'烟尘(Rtd)') > 0:
        Line2 = Line2 + str.split(u'烟尘(Rtd)')[1].split('mg/m3')[0] + ';'
    else:
        Line2 = Line2 + ';'
    if str.find(u'烟气流速(Rtd)') > 0:
        Line2 = Line2 + str.split(u'烟气流速(Rtd)')[1].split('m/s')[0] + ';'
    else:
        Line2 = Line2 + ';'
    if str.find(u'烟气压力(Rtd)') > 0:
        Line2 = Line2 + str.split(u'烟气压力(Rtd)')[1].split('kpa')[0] + ';'
    else:
        Line2 = Line2 + ';'
    if str.find(u'烟气温度(Rtd)') > 0:
        Line2 = Line2 + str.split(u'烟气温度(Rtd)')[1].split(u'℃')[0] + ';'
    else:
        Line2 = Line2 + ';'
    if str.find(u'废气流量(Rtd)') > 0:
        Line2 = Line2 + str.split(u'废气流量(Rtd)')[1].split('m3/s')[0] + ';'
    else:
        Line2 = Line2 + ';'
    if str.find(u'烟气湿度(Rtd)') > 0:
        Line2 = Line2 + str.split(u'烟气湿度(Rtd)')[1].split('%')[0] + ';'
    else:
        Line2 = Line2 + ';'
    Line = Line1 + '\n' + Line2
    print Line
    try:
        file = open('webdata1.txt', 'w')
        file.write(Line.encode('gbk'))
    finally:
        file.close()
    if Line.find(u'当前监控点无数据') < 0:
        pass
    else:
        print  "页面失效，尝试重新登陆。。。"
        load()
    print "等待60秒后重新抓取。。。"
    time.sleep(60)
    # pa=re.compile(u'当前监控')
    # while 1>0:
    #     # 荆州市集美热电有限责任公司废气排放口1
    #     Line1="1#;"+Crawler(postdata1)
    #     # 荆州市集美热电有限责任公司废气排放口2
    #     Line2="2#;"+Crawler(postdata2)
    #     Line=Line1+Line2
    #     # print type(Line)
    #     print Line
    #     # Line.decode(unicode)
    #     #Line=unicodedata.normalize('NFKD',Line).encode('ascii','ignore')
    #     # print(type(Line))
    #     file = open('webdata1.txt', 'a')
    #     file.write(Line.encode('gbk'))
    #     if pa.findall(Line):
    #         file.write('有BUG，重新登录')
    #         load()
    #     else:
    #         file.close()
    #     time.sleep(60)
