# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class KsshopdataItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    keyword = scrapy.Field()
    page = scrapy.Field()
    kwaiId = scrapy.Field()
    user_id = scrapy.Field()
    user_name = scrapy.Field()
    user_sex = scrapy.Field()
    phone_number = scrapy.Field()
    wechart_number = scrapy.Field()
    verified = scrapy.Field()
    verified_infomoation= scrapy.Field()
    cityName = scrapy.Field()
    constellation = scrapy.Field()
    fans = scrapy.Field()
    follow = scrapy.Field()
    work = scrapy.Field()
    xiao_shop = scrapy.Field()
    shop_product_number = scrapy.Field()
    link = scrapy.Field()

