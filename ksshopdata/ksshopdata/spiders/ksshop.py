# -*- coding: utf-8 -*-
import scrapy
import copy
import json
from ..items import KsshopdataItem
import re
import logging

class KsshopSpider(scrapy.Spider):
    name = 'ksshortshop'
    shop_url = 'https://wxmini-api.uyouqu.com/rest/wd/search/user'
    info_url = 'https://wxmini-api.uyouqu.com/rest/wd/wechatApp/user/profile'
    shop_data = {
        "keyword": "",
        "pcursor": None,
        "ussid": None
    }
    info_data  ={
        "eid": ""
    }
    def start_requests(self):
        f = open(r"C:\Users\honey\Desktop\keywords.txt", encoding='utf-8')
        keywords_list = f.readline()[1:].split(",")
        f.close()
        for keyword in keywords_list:
            item = KsshopdataItem()
            # shop_headers = copy.deepcopy(self.headers)
            shop_data = copy.deepcopy(self.shop_data)
            shop_data['keyword'] = keyword
            item['keyword'] = keyword
            print('*****正在爬取%s关键词的第%s页用户信息*****'%(keyword,"0"))
            yield scrapy.Request(url=self.shop_url,method ="POST",body=json.dumps(shop_data),callback=self.parse,meta={'item': copy.deepcopy(item)})

    def parse(self, response):
        item = response.meta['item']
        shop_info = json.loads(response.text)
        if  shop_info['result'] == 1:
            if not shop_info['pcursor'] == 'no_more':
                item['page'] = str(int(shop_info['pcursor'])-1)
            else:
                item['page'] = item['page']
            ussid = shop_info['ussid']
            for shop in shop_info['users']:
                try:
                    item['kwaiId'] = shop['kwaiId']
                except:
                    item['kwaiId'] = ""
                else:
                    item['kwaiId'] = shop['kwaiId']
                item['user_id'] = shop['user_id']
                item['user_name'] = shop['user_name']
                item['user_sex'] = shop['user_sex']
                try:
                    item['phone_number'] = "、".join(re.findall('[0-1][0-9]{2}[\s|-|_]?[0-9]{4}[\s|-|_]?[0-9]{4}',item['user_name']+","+shop['user_text']+","+item['kwaiId'],re.S))
                except:
                    item['phone_number'] = ""
                else:
                    item['phone_number'] = "、".join(re.findall('[0-1][0-9]{2}[\s|-|_]?[0-9]{4}[\s|-|_]?[0-9]{4}', item['user_name']+","+shop['user_text']+","+item['kwaiId'], re.S))
                item['verified'] = shop['verified']
                try:
                    item['verified_infomoation'] = shop['verifiedDetail']['description'].split()[-1]
                except:
                    item['verified_infomoation'] = " "
                else:
                    item['verified_infomoation'] = shop['verifiedDetail']['description'].split()[-1]
                item['link'] = "https://live.kuaishou.com/profile/"+item['kwaiId'] if not item['kwaiId'] == "" else ""
                print('*****%s关键词的第%s页的%s的用户信息已经爬取完成!*****' % (item['keyword'], item['page'], item['user_id']))
                yield item

            if not str(shop_info['pcursor']) == "no_more":
                shop_data = copy.deepcopy(self.shop_data)
                shop_data['keyword'] = item['keyword']
                shop_data["pcursor"] = shop_info['pcursor']
                item['page'] = shop_data["pcursor"]
                shop_data['ussid'] = ussid
                print('*****正在爬取%s关键词的第%s页用户信息*****' % (item['keyword'],item['page']))
                yield scrapy.Request(url=self.shop_url,method ="POST",body=json.dumps(shop_data),callback=self.parse,meta={'item': copy.deepcopy(item)})

        else:
            print("此次请求出错！")
            logging.error(shop_info['error_msg'])



    # def info_parse(self,response):
    #     item = response.meta['item']
    #     info_dic = json.loads(response.text)
    #     result = info_dic['result']
    #     if result == 1:
    #         info_data = info_dic['userProfile']
    #         try:
    #             item['cityName'] = info_data['cityName']
    #         except:
    #             item['cityName'] = ""
    #         else:
    #             item['cityName'] = info_data['cityName']
    #         try:
    #             item['constellation'] = info_data['constellation']
    #         except:
    #             item['constellation'] = ""
    #         else:
    #             item['constellation'] = info_data['constellation']
    #         item['fans'] =info_data['ownerCount']['fan']
    #         item['follow'] = info_data['ownerCount']['follow']
    #         item['work'] = info_data['ownerCount']['photo']
    #         print('*****%s关键词的第%s页的%s的用户信息已经爬取完成!*****' % (item['keyword'], item['page'], item['user_id']))
    #         yield item
    #     else:
    #         print("此次请求出错！")
    #         print(info_dic['error_msg'])
    #         yield item
