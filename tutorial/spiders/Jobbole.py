# -*- coding: utf-8 -*-
import scrapy

import sys
try:
    import urlparse  # python2
    reload(sys)
    sys.setdefaultencoding('utf-8')  # 修改默认编码
except:
    from urllib import parse as urlparse   # python3
from scrapy.http import Request # 带入Request方法继续请求解析出的页面
from tutorial.items import JobboleItem # 实例化items


class JobboleSpider(scrapy.Spider):
    name = 'Jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']


    def parse(self, response):
        links = response.css('a.archive-title')
        for link in links: # 拿到所有文章url
            link = link.css('::attr(href)').extract_first('error')
            # print urlparse.urljoin(response.url, link)
            yield Request(url=urlparse.urljoin(response.url, link), callback=self.parse_content)

        next_url = response.css('.next.page-numbers::attr(href)').extract_first() # 下一页
        if next_url:
            print urlparse.urljoin(response.url, next_url)
            yield Request(url=urlparse.urljoin(response.url, next_url), callback=self.parse)


    def parse_content(self, response):
        items = JobboleItem()
        title = response.css('.entry-header h1::text').extract_first('error')
        main_tags = response.css('.entry ::text').extract()
        content = ''
        for i in main_tags: content += i;
        creat_time = response.css('.entry-meta p::text').extract_first('error').strip()[:-1].strip() # 创始时间

        items['page_url'] = response.url
        items['page_title'] = title
        items['page_content'] = content
        items['page_create_time'] = creat_time

        yield items
