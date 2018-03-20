# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from tutorial import sql_setting
from tutorial.mysql_orm import add_data # 调用orm映射

class TutorialPipeline(object):

    def process_item(self, item, spider):
        data = {}
        if spider.name == 'baike_key':
            sql = sql_setting.Sql()
            data['url'] = item['url']
            data['title'] = item['title']
            data['para'] = item['para']
            sql.sql_cennector(data)

        else:
            data['url'] = item['page_url']
            data['title'] = item['page_title']
            data['content'] = item['page_content']
            data['create_time'] = item['page_create_time']
            add_data(data)

        return item
