#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Morrow
# @IDE     : PyCharm
# @File    : main.py
# @Email   : 464580843@qq.com
# Create on 2018/3/18 0018 20:40
'''
方便ide调试
'''
from scrapy.cmdline import execute
import sys
import os

print os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# execute(['scrapy','crawl','baike_key','-s','CLOSESPIDER_TIMEOUT=3600'])

# -s CLOSESPIDER_TIMEOUT=18000  设置5小时后关闭爬虫
execute(['scrapy','crawl','Jobbole','-s','CLOSESPIDER_TIMEOUT=18000'])