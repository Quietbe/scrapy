# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class NewSpiderPipeline(object):
    def process_item(self, item, spider):
        return item


class New_spiderPipeline(object):

    def open_spider(self,spider):
        self.file = open('北京.json','w')

    def  close_spider(self,spider):
        self.file.close()

    def process_item(self, item, spider):

        # print(item['city'])
        #城市
        city = item['city']['display']
        #页面地址
        url = item['positionURL']
        #工资
        salary = item['salary']
        #公司名称
        name = item['company']['name']
        #工作名称
        jobName = item['jobName']

        content = {
            'city'    : city,
            'url'     : url,
            'salary'  :salary,
            'name'    :name,
            'jobName' : jobName
        }
        self.file.write(str(content)+',\n')

