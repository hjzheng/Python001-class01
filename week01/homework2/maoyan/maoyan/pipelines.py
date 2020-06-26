# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MaoyanPipeline:
    # def process_item(self, item, spider):
    #     return item

    # 每一个item管道组件都会调用该方法，并且必须返回一个item对象实例或raise DropItem异常
    def process_item(self, item, spider):
        fname = item['fname']
        ftype = item['ftype']
        fdate = item['fdate']

        output = f'|{fname.strip()}|\t|{ftype.strip()}|\t|{fdate.strip()}|\n\n'

        print(output)

        with open('./maoyanfilm.txt', 'a+', encoding='utf-8') as article:
            article.write(output)
            article.close()

        return item
