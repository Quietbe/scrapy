# -*- coding: utf-8 -*-
import scrapy
import re
import json

class S1Spider(scrapy.Spider):
    name = 'S_1'
    # allowed_domains = ['baidu.com']
    #start 开始起点   pageSize 请求容量
    start_urls = ['https://fe-api.zhaopin.com/c/i/sou?start=0&pageSize=60&cityId=530&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&jobType=044&kt=3&_v=0.76016843&x-zp-page-request-id=95a691082cc34ae18bdf2595858e4dd1-1553157701991-11773']

    def parse(self, response):

        # js = json.loads(response.text)
        # tx = open('json.json','w')
        # tx.write(response.text)
        # tx.close()

        str = response.text
        content = re.search('results":(.*?),"debugInfo',str,re.S).group(1)
        ## 职位页面url
        # url = re.findall('positionURL:"(.*?)"',content,re.S)
        #
        content = json.loads(content)
        # print(content[0]['city'])
        for i in content:
            yield i

        # print(js)


























#
#
# ip地址查询接口
#  腾讯IP地址查询接口：http://fw.qq.com/ipaddress
# 新浪IP地址查询接口：http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=js
# 搜狐IP地址查询接口：http://pv.sohu.com/cityjson
# 谷歌IP地址查询接口：http://j.maxmind.com/app/geoip.js  未验证
# 有道IP地址查询接口：http://www.youdao.com/smartresult-xml/search.s
# 1616 IP地址查询接口：http://w.1616.net/chaxun/iptolocal.php
# 126   http://ip.ws.126.net/ipquery
# hao123  http://app.hao123.com/ipquery/getcity.php?rtype=2
# ---------------------
# 作者：凡尘炼心
# 来源：CSDN
# 原文：https://blog.csdn.net/q669239799/article/details/80782928
# 版权声明：本文为博主原创文章，转载请附上博文链接！