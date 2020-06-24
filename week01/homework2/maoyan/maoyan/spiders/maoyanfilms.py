# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup as bs

from maoyan.items import MaoyanItem


class MaoyanfilmsSpider(scrapy.Spider):
    name = 'maoyanfilms'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/']

    # def parse(self, response):
    #     pass

    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, callback=self.parse)
        # url 请求访问的网址
        # callback 回调函数，引擎回将下载好的页面(Response对象)发给该方法，执行数据解析
        # 这里可以使用callback指定新的函数，不是用parse作为默认的回调参数

    # 解析函数
    def parse(self, response):
        soup = bs(response.text, 'html.parser')

        divstag = soup.find_all(
            'div', attrs={'class': 'movie-item-hover'}, limit=10)

        for divtag in divstag:
            item = MaoyanItem()
            item['fname'] = divtag.find('span', attrs={'class': 'name'}).text

            for span in divtag.find_all('span', attrs={'class': 'hover-tag'}):
                txt = span.text
                if txt == '类型:':
                    item['ftype'] = span.next_sibling
                if txt == '上映时间:':
                    item['fdate'] = span.next_sibling
            yield item
