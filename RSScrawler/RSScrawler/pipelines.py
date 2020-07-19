# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class RsscrawlerPipeline(object):


    def open_spider(self,spider):
        self.file = open('../../Q1/description.txt', 'w')
 
    def close_spider(self,spider):
        self.file.close()

    def process_item(self, item, spider):
        try:
            line = item["description"]
            
            self.file.write(line+"\n")
        except:

            raise