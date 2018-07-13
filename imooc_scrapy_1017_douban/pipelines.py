# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from imooc_scrapy_1017_douban.settings import mongodb_host,mongodb_port,mongodb_name,mongodb_collection
class ImoocScrapy1017DoubanPipeline(object):
    def __init__(self):
        host = mongodb_host
        port = mongodb_port
        dbname = mongodb_name
        sheetname = mongodb_collection
        client = pymongo.MongoClient(host, port)
        mydb = client[dbname]
        self.post = mydb[sheetname]


    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item
