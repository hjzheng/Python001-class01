# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector

from maoyan.items import MaoyanItem


class MaoyanfilmsSpider(scrapy.Spider):
    name = 'maoyanfilms'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/']

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
        div_tags = Selector(response=response).xpath(
            '//div[@class="movie-hover-info"]')
        index = 0

        for div_tag in div_tags:

            if index >= 10:
                break

            index += 1

            item = MaoyanItem()
            fname = div_tag.xpath(
                './/div[@class="movie-hover-title"][1]/span[1]/text()')
            ftype = div_tag.xpath(
                './/div[@class="movie-hover-title"][2]/text()')
            fdate = div_tag.xpath(
                './/div[@class="movie-hover-title movie-hover-brief"]/text()')

            item['fname'] = fname.extract()[0]
            item['ftype'] = ftype.extract()[1]
            item['fdate'] = fdate.extract()[1]

            yield item
