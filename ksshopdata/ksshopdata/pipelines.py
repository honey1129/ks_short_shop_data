# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import csv
import time

class KsshopdataPipeline(object):
    fp = None

    def open_spider(self, spider):
        f = open(r"C:\Users\honey\Desktop\keywords.txt", encoding='utf-8')
        keyword = f.readline()[1:].split(',')
        keyword = ",".join(keyword) if len(keyword) < 4 else ",".join(keyword[:4])+"等"
        f.close()
        self.fp = open(time.strftime('%Y%m%d%H%M%S')+keyword+'ks_data.csv', 'w', encoding='utf_8_sig', newline="",)
        writer = csv.writer(self.fp)
        writer.writerow(["名称", "性别", "id","快手号","主页链接","联系电话",
                          "是否蓝V","页码","关键词"])

    def process_item(self, item, spider):
        writer = csv.writer(self.fp)
        if not item['verified'] and not item['phone_number']=="":
            writer.writerow(
                [item['user_name'], item['user_sex'], item['user_id'], item['kwaiId'],item['link'],item['phone_number'],item['verified'], item["page"], item["keyword"]])
            return item
    def close_spider(self, spider):
        self.fp.close()