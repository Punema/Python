# -*- coding:utf-8 -*-
import urllib
import urllib2
import re

class BDTB:
    #初始化，传入基地址，是否只看楼主的参数
    def __init__(self,baseUrl,seeLZ):
        self.baseURL = baseUrl
        self.seeLZ = '?See_lz='+str(seeLZ)

    #传入页码，获取该页帖子的代码
    def getPage(self,pageNum):
        try:
            url = self.baseURL + self.seeLZ + '&pn=' + str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            print response.read()
            return response.read().decode('utf-8')
        except urllib2.URLError,e:
            if hasattr(e,"reason"):
                print u"连接百度贴吧失败，错误原因",e.reason
                return None

    # 获取帖子标题
    def getTitle(self):
        page = self.getPage(1)
        pattern = re.compile('<h3 class ="core_title_txt pull-left.*?>(.*?)</h3>', re.S)
        result = re.search(pattern, page)
        if result:
            print result.group(1)  #测试输出
            return result.group(1).strip()
        else:
            return None

baseURL = 'https://tieba.baidu.com/p/3138733512'
batb = BDTB(baseURL,1)
#batb.getPage(1)
page = batb.getPage(1)
pattern = re.compile('<h3 class ="core_title_txt pull-left.*?>(.*?)</h3>', re.S)
result = re.search(pattern, page)
print result