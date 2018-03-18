# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from tutorial import sql_setting

class TutorialPipeline(object):
    def process_item(self, item, spider):
        data = {}
        sql = sql_setting.Sql()
        data['url'] = item['url']
        data['title'] = item['title']
        data['para'] = item['para']

        sql.sql_cennector(data)

        return item
