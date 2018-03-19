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
from tutorial.items import TutorialItem # 实例化items



class BaikeKeySpider(scrapy.Spider):
    name = 'baike_key'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baike.baidu.com/item/python']

    def parse(self, response):

        print "crwal: " + response.url

        tt_item = TutorialItem()
        page_url = response.url
        links = response.selector.re(r'href="(/item/[\w%]+)"') # response自带正则解析
        for link in links:
            next_url = urlparse.urljoin(page_url, link)
            yield Request(next_url)

        # title = response.xpath('//dd[@class="lemmaWgt-lemmaTitle-title"]/h1/text()').extract_first('error')
        title = response.css('div .lemmaWgt-lemmaTitle-title h1::text').extract_first('error: not found')
        # para_lst = response.xpath('//div[@class="lemma-summary"]/div[@class="para"]//text()').extract()
        para_lst = response.css('div .lemma-summary div.para ::text').extract()
        para = ''
        for i in para_lst:para += i;

        tt_item['url'] = page_url
        tt_item['title'] = title
        tt_item['para'] = para

        yield tt_item