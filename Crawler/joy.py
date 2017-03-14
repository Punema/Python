# -*- coding:utf-8 -*-
import urllib
import urllib2
import re

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
#item[0] 用户名
#item[1] 内容
#item[2] 图片
#item[3] 好笑数
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile(
        '<div class="author clearfix">.*?href.*?<img src.*?title=.*?<h2>(.*?)</h2>.*?<div class="content">.*?<span>(.*?)</span>.*?</div>'+
        '(.*?)'+
        '<i class="number">(.*?)</i>',re.S)
    items = re.findall(pattern, content)

    for item in items:
        haveImg = re.search("img", item[2])
        if not haveImg:
            print item[0]
            print item[1]
            print item[3]
            print
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason