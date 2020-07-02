# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

# 假设数据库已经创建 DB maoyanfilm

# CREATE TABLE `maoyanfilm` (
#   `id` bigint(20) NOT NULL AUTO_INCREMENT,
#   `name` varchar(200) DEFAULT NULL,
#   `type` varchar(200) DEFAULT NULL,
#   `date` varchar(200) DEFAULT NULL,
#   PRIMARY KEY (`id`)
# ) ENGINE=InnoDB AUTO_INCREMENT=1578 DEFAULT CHARSET=utf8;


class MaoyanPipeline:
    # def process_item(self, item, spider):
    #     return item

    # 每一个item管道组件都会调用该方法，并且必须返回一个item对象实例或raise DropItem异常
    def process_item(self, item, spider):
        fname = item['fname']
        ftype = item['ftype']
        fdate = item['fdate']

        # output = f'{fname.strip()},{ftype.strip()},{fdate.strip()}\n'

        # with open('./maoyanfilm.csv', 'a+', encoding='utf-8') as article:
        #     article.write(output)
        #     article.close()

        # 写入数据库
        conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='---',
            db='test'
        )

        sql = f"insert into maoyanfilm (name, type, date) values ('{fname.strip()}','{ftype.strip()}','{fdate.strip()}')"

        print(sql)
        # 游标建立的时候就开启了一个隐形的事物
        cur = conn.cursor()
        try:
            cur.execute(sql)
            conn.commit()
        except:
            conn.rollback()
        # 关闭数据库连接
        conn.close()

        return item
