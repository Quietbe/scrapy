# -*- coding: utf-8 -*-
import scrapy
import re


class DemoSpider(scrapy.Spider):
    name = 'demo'
    start_urls = ['https://sou.zhaopin.com/']

    def parse(self, response):
        urlList = re.findall('软件/互联网开发/系统集成</a>(.*?)<div style="display', response.body, re.S)[0]
        urlList = re.findall("jobnavfold'\);\" href=\"(.*?)\" target", urlList, re.S)
        u = "http://sou.zhaopin.com"

        for each in urlList:
            each = u+each
            a = re.search('jl=(.*?)&bj=',each,re.S).group(1)

            # 设置爬取范围
            for c in range(530, 933):
                c = str(c)
                uu = each.replace(a, c)
                yield scrapy.Request(uu, callback=self.parser_find)

    def parser_find(self, response):
        u = "http://sou.zhaopin.com/jobs/searchresult.ashx?"
        url = re.search("<a href=\"http://sou.zhaopin.com/jobs/searchresult.ashx\?(.*?)2\">2</a>", response.body,
                        re.S).group(1)
        # url = "href=\""+u+"(.*?)p=2\">2</a>"
        url = u + url
        yield scrapy.Request(url, callback=self.parser_start)

        # 构造地址翻页

    def parser_start(self, response):
        url = response.url
        shu = re.search("<em>(.*?)</em>", response.body, re.S).group(1)
        x = (int(shu) / 60) + 1
        for href in range(x):
            href = url + str(href)
            yield scrapy.Request(href, callback=self.parser_save)
        print 'The end of the Parser Work'

    def parser_save(self, response):
        body = response.body
        zpList = {}
        b = re.findall('<td class="zwmc"(.*?)</table>', body, re.S)
        x = 1
        for each in b:
            zpList[x]=each
            x=x+1
        yield zpList
