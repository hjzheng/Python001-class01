# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
from douban.items import DoubanItem


class DoubanfilmsSpider(scrapy.Spider):
    name = 'doubanfilms'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def start_requests(self):
        for i in range(10):
            url = f'https://movie.douban.com/top250?start={i*25}'
            print(url)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        div_tags = Selector(response=response).xpath('//div[@class="hd"]')

        for div_tag in div_tags:
            item = DoubanItem()
            furl = div_tag.xpath('.//a/@href')
            fname = div_tag.xpath('.//a/span[@class="title"]/text()')
            item['fname'] = fname.extract_first().strip()
            item['furl'] = furl.extract_first().strip()

            yield scrapy.Request(url=item['furl'], meta={'item': item}, callback=self.detailParse)

    def detailParse(self, response):

        item = response.meta['item']

        fcontent = Selector(response=response).xpath(
            '//span[@property="v:summary"]/text()')

        item['fcontent'] = fcontent.extract_first().strip()

        yield item
