# -*- coding: utf-8 -*-
import scrapy
import sys
import re
from lxml import etree
try:
    import urlparse  # python2
except:
    from urllib import parse as urlparse   # python3
from scrapy.http import Request
from tutorial.items import TutorialItem
reload(sys)
sys.setdefaultencoding('utf-8') # 修改默认编码



class BaikeKeySpider(scrapy.Spider):
    name = 'baike_key'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baike.baidu.com/item/qq']

    def parse(self, response):

        print 'crawl:'+ response.url

        tt_item = TutorialItem()
        html = etree.HTML(response.body)
        page_url = response.url
        regex = re.compile(r'href="(/item/[\w%]+)"')
        links = re.findall(regex, response.body)
        for link in links:
            next_url = urlparse.urljoin(page_url, link)
            yield Request(next_url)

        title = html.xpath('//dd[@class="lemmaWgt-lemmaTitle-title"]/h1/text()')
        para_lst = html.xpath('//div[@class="lemma-summary"]/div[@class="para"]/text()')
        para = ''
        for i in para_lst:para += i;

        tt_item['url'] = page_url
        tt_item['title'] = title[0]
        tt_item['para'] = para

        yield tt_item