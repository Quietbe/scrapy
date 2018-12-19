# -*- coding: utf-8 -*-
import scrapy


class StocksSpider(scrapy.Spider):
    name = 'Stocks'
    start_urls = ['https://sou.zhaopin.com/?pageSize=60&jl=530&kw=Python&kt=3']

    def parse(self, response):

        aaa = {}
        aaa.update({'a':'111'})
        aaa.update({'b':'222'})
        aaa.update({'c':'333'})

        yield aaa



