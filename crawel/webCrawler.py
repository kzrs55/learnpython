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
# �漰���ĸ�ҳ���ַ
mainurl = 'http://119.97.194.18:4503/'
hosturl = 'http://119.97.194.18:4503/Default.aspx'
imgurl = 'http://119.97.194.18:4503/ImageCode.aspx'
# �ŷſ�1
# finalurl='http://119.97.194.18:4503/pcSingleData/LastData.aspx?StationName=%be%a3%d6%dd%ca%d0%bc%af%c3%c0%c8%c8%b5%e7%d3%d0%cf%de%d4%f0%c8%ce%b9%ab%cb%be%b7%cf%c6%f8%c5%c5%b7%c5%bf%da%a3%a31'
# �ŷſ�2
# finalurl='http://119.97.194.18:4503/pcSingleData/LastData.aspx?StationName=%be%a3%d6%dd%ca%d0%bc%af%c3%c0%c8%c8%b5%e7%d3%d0%cf%de%d4%f0%c8%ce%b9%ab%cb%be%b7%cf%c6%f8%c5%c5%b7%c5%bf%da%a3%a32'
# last
# finalurl='http://119.97.194.18:4503/pcSingleData/LastData.aspx?StationName=%ba%fe%b1%b1%cb%c9%d4%b4%ed%b7%ca%af%b7%a2%b5%e7%d3%d0%cf%de%b9%ab%cb%be(%d7%dc%c5%c5%bf%da%d7%b0%bb%fa%c8%dd%c1%bf2.5%cd%f2%c7%a7%cd%df)'
finalurl = 'http://119.97.194.18:4503/pcSingleData/LastData.aspx'
stationname2 = '%be%a3%d6%dd%ca%d0%bc%af%c3%c0%c8%c8%b5%e7%d3%d0%cf%de%d4%f0%c8%ce%b9%ab%cb%be%b7%cf%c6%f8%c5%c5%b7%c5%bf%da%a3%a32'
stationname1 = '%be%a3%d6%dd%ca%d0%bc%af%c3%c0%c8%c8%b5%e7%d3%d0%cf%de%d4%f0%c8%ce%b9%ab%cb%be%b7%cf%c6%f8%c5%c5%b7%c5%bf%da%a3%a31'
# ����config����
conf = ConfigParser.ConfigParser()
# ��config�����ȡ�����ļ�
conf.read("crawler.cfg")
# ָ��section��option��ȡֵ
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
# ��ʼ��һ��CookieJar������Cookie����Ϣ#
cookie = cookielib.CookieJar()
# ����һ���µ�opener��ʹ�����ǵ�CookieJar#
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

        # ʶ��������֤��
        im = Image.open(myimg)
        mycode = pytesseract.image_to_string(im)
        # ģ���½ҳ�� ������ȡ��½�󷵻ص�ҳ��
        loginpostData = {
            '__VIEWSTATE': '/wEPDwUKLTQ5NjAyMzY4Nw8WAh4IcGFzc2NvZGUFBDk1MDdkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYBBQZjaGtSZW1y7jFce70qxCpFrAi8Zjpn3OkM82lDcMs4ttBf44VqKg==',
            # һ�ѱ��룬�ݲ�֪��������
            '__EVENTVALIDATION': '/wEWBwKq+bGyAQLYzu/ODgKl1bKzCQK1qbSWCwKIwcnbDwKK+ragDQLb18frA3HdAgeoCC+HsJrGpQtloOQHmAgodvZXNlh+d+eGiI1d',
            # ����һ�ѱ��룬�ݲ�֪��������
            'hidUserScreenWidth': 1920,
            'txtUserName': user,
            'txtPassWord': password,
            'txtImgCode': mycode,
            'ibtnOK': '��½'
        }
        loginpostData = urllib.urlencode(loginpostData)
        request = urllib2.Request(hosturl, loginpostData, loginheaders)
        response = urllib2.urlopen(request)
        text = response.read()
        pattern = re.compile('�����м����ȵ��������ι�˾����')  # ͨ��������ȡ����ҳ���ж��Ƿ��½�ɹ���Ӧ���и����ķ���
        if pattern.findall(text):
            print "��½�ɹ�������"
            boolean = False
        else:
            print "��½ʧ�ܡ�����"


print "���ڵ�¼������"
load()
print "��ʼ��ȡ����"
while 1 > 0:
    # �����м����ȵ��������ι�˾�����ŷſ�1
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
    if str.find(u'O2����(Rtd)') > 0:
        Line1 = Line1 + str.split(u'O2����(Rtd)')[1].split('%')[0] + ';'
    else:
        Line1 = Line1 + ';'
    if str.find(u'�̳�(ZsRtd)') > 0:
        Line1 = Line1 + str.split(u'�̳�(ZsRtd)')[1].split('mg/m3')[0] + ';'
    else:
        Line1 = Line1 + ';'
    if str.find(u'�̳�(Rtd)') > 0:
        Line1 = Line1 + str.split(u'�̳�(Rtd)')[1].split('mg/m3')[0] + ';'
    else:
        Line1 = Line1 + ';'
    if str.find(u'��������(Rtd)') > 0:
        Line1 = Line1 + str.split(u'��������(Rtd)')[1].split('m/s')[0] + ';'
    else:
        Line1 = Line1 + ';'
    if str.find(u'����ѹ��(Rtd)') > 0:
        Line1 = Line1 + str.split(u'����ѹ��(Rtd)')[1].split('kpa')[0] + ';'
    else:
        Line1 = Line1 + ';'
    if str.find(u'�����¶�(Rtd)') > 0:
        Line1 = Line1 + str.split(u'�����¶�(Rtd)')[1].split(u'��')[0] + ';'
    else:
        Line1 = Line1 + ';'
    if str.find(u'��������(Rtd)') > 0:
        Line1 = Line1 + str.split(u'��������(Rtd)')[1].split('m3/s')[0] + ';'
    else:
        Line1 = Line1 + ';'
    if str.find(u'����ʪ��(Rtd)') > 0:
        Line1 = Line1 + str.split(u'����ʪ��(Rtd)')[1].split('%')[0] + ';'
    else:
        Line1 = Line1 + ';'


    # �����м����ȵ��������ι�˾�����ŷſ�2
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
    if str.find(u'O2����(Rtd)') > 0:
        Line2 = Line2 + str.split(u'O2����(Rtd)')[1].split('%')[0] + ';'
    else:
        Line2 = Line2 + ';'
    if str.find(u'�̳�(ZsRtd)') > 0:
        Line2 = Line2 + str.split(u'�̳�(ZsRtd)')[1].split('mg/m3')[0] + ';'
    else:
        Line2 = Line2 + ';'
    if str.find(u'�̳�(Rtd)') > 0:
        Line2 = Line2 + str.split(u'�̳�(Rtd)')[1].split('mg/m3')[0] + ';'
    else:
        Line2 = Line2 + ';'
    if str.find(u'��������(Rtd)') > 0:
        Line2 = Line2 + str.split(u'��������(Rtd)')[1].split('m/s')[0] + ';'
    else:
        Line2 = Line2 + ';'
    if str.find(u'����ѹ��(Rtd)') > 0:
        Line2 = Line2 + str.split(u'����ѹ��(Rtd)')[1].split('kpa')[0] + ';'
    else:
        Line2 = Line2 + ';'
    if str.find(u'�����¶�(Rtd)') > 0:
        Line2 = Line2 + str.split(u'�����¶�(Rtd)')[1].split(u'��')[0] + ';'
    else:
        Line2 = Line2 + ';'
    if str.find(u'��������(Rtd)') > 0:
        Line2 = Line2 + str.split(u'��������(Rtd)')[1].split('m3/s')[0] + ';'
    else:
        Line2 = Line2 + ';'
    if str.find(u'����ʪ��(Rtd)') > 0:
        Line2 = Line2 + str.split(u'����ʪ��(Rtd)')[1].split('%')[0] + ';'
    else:
        Line2 = Line2 + ';'
    Line = Line1 + '\n' + Line2
    print Line
    try:
        file = open('webdata1.txt', 'w')
        file.write(Line.encode('gbk'))
    finally:
        file.close()
    if Line.find(u'��ǰ��ص�������') < 0:
        pass
    else:
        print  "ҳ��ʧЧ���������µ�½������"
        load()
    print "�ȴ�60�������ץȡ������"
    time.sleep(60)
    # pa=re.compile(u'��ǰ���')
    # while 1>0:
    #     # �����м����ȵ��������ι�˾�����ŷſ�1
    #     Line1="1#;"+Crawler(postdata1)
    #     # �����м����ȵ��������ι�˾�����ŷſ�2
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
    #         file.write('��BUG�����µ�¼')
    #         load()
    #     else:
    #         file.close()
    #     time.sleep(60)
