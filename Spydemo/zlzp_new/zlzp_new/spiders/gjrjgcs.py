# -*- coding: utf-8 -*-
import scrapy
import re


class GjrjgcsSpider(scrapy.Spider):
    name = 'gjrjgcs'
    start_urls = ['http://sou.zhaopin.com/jobs/searchresult.ashx?jl=530&bj=160000&sj=044']

    def parse(self, response):

        url= 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl='
        c = '&bj=160000&sj=044'
        for n in range(530,933):
            n = url+str(n)+c
            yield scrapy.Request(n, callback=self.parser_find)

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