# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanPipeline:
    def process_item(self, item, spider):
        fname = item['fname']
        furl = item['furl']
        fcontent = item['fcontent']

        output = f'{fname},{furl},{fcontent}\n'

        with open('./doubanfilm.csv', 'a+', encoding='utf-8') as article:
            article.write(output)
            article.close()

        return item
