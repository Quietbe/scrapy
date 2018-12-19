# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
import MySQLdb
import time

class SpydemoPipeline(object):
    def process_item(self, item, spider):
        for each in item:
            print each

# 自写
class Spydemo_demoPinpeline(object):
    StartTime = time.time()
    EndTime = 0
    # def open_spider(self,spider):
    #     global StartTime
    #     StartTime = time.time()
    #
    # def close_spider(self,spider):
    #     global EndTime,StartTimes
    #     EndTime = time.time()
    #     WorkingTime = EndTime-StartTime
    #     WorkingTime = float(WorkingTime/3600)
    #     print 'The end of the Parser Work,the spider Worked for %s Hours' % (WorkingTime)
    def process_item(self,item,spider):
        try:
            for each in item:
                a = item[each]
                name = re.findall('target="_blank">(.*?)</a>', a, re.S)[0]
                gz = re.findall('class="zwyx">(.*?)</td>', a, re.S)[0]
                gzdd = re.findall('class="gzdd">(.*?)</td>', a, re.S)[0]
                gsxz = re.findall('公司性质：(.*?)<', a, re.S)[0]
                gsgm = re.findall('公司规模：(.*?)<', a, re.S)[0]
                xl = re.findall('span>学历：(.*?)<', a, re.S)[0]
                bz = re.findall('newlist_deatil_last">(.*?)</li>', a, re.S)[0]
                href = re.findall('href="(.*?)" target=', a, re.S)[0]
                db = MySQLdb.connect('localhost', 'root', '', 'test', charset='utf8')
                cursor = db.cursor()
                sql = "INSERT INTO zlzp_demo (name,gz,gzdd,gsxz,gsgm,xl,bz,href) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s')" % (
                name, gz, gzdd, gsxz, gsgm, xl, bz, href)

                cursor.execute(sql)
                db.commit()
                print 'Insert Data Success'
        except:
            db.rollback()
            print 'one error'
        db.close()
        global StartTime
        WorkingTime = float((time.time()-StartTime)/3600)
        print 'The end of the Parser Work,the spider Worked for %s Hours' % (WorkingTime)

# class Spydemo_StocksPinpeline(object):
#
#     def process_item(self,item,spider):
#
#         print item
