# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    para = scrapy.Field()
    pass

class JobboleItem(scrapy.Item):
    page_url = scrapy.Field()
    page_title = scrapy.Field()
    page_content = scrapy.Field()
    page_create_time = scrapy.Field()
