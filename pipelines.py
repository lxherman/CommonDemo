# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import time
from sshtunnel import SSHTunnelForwarder

class MysqlPipeline(object):
    def __init__(self, host, database, user, password, port):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('MYSQL_HOST'),
            database=crawler.settings.get('MYSQL_DATABASE'),
            user=crawler.settings.get('MYSQL_USER'),
            password=crawler.settings.get('MYSQL_PASSWORD'),
            port=crawler.settings.get('MYSQL_PORT'),
        )

    def open_spider(self, spider):
        self.db = pymysql.connect(self.host,self.user,self.password,self.database,charset='utf8',port=self.port)
        self.cursor = self.db.cursor()

    def close_spider(self, spider):
        self.db.close()

    def process_item(self, item, spider):
        data = dict(item)
        keys = ','.join(data.keys())
        values = ','.join(['%s'] * len(data))
        sql = 'INSERT INTO {table}({keys}) values({values})'.format(table=item.table, keys=keys, values=values)
        try:
            if self.cursor.execute(sql, tuple(data.values())):
                self.db.commit()
                print('==》入库成功')
        except:
            try:
                # now_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
                id = list(data.values())[0]
                id_name = list(data.keys())[0]
                # sql2 = "UPDATE {table} SET updateTime = '{time}',isOnline = 1 WHERE {id_name} = '{id}'".format(table = item.table, time = now_time, id_name = id_name, id = id)
                sql2 = "UPDATE {table} SET isOnline = 1 WHERE {id_name} = '{id}'".format(table = item.table, id_name = id_name, id = id)
                if self.cursor.execute(sql2):
                    self.db.commit()
                    print('--》更新成功')
            except:
                print('__>入库失败')
                self.db.rollback()

        return item


