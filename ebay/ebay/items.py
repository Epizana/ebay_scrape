# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import re


class EbayItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    #ebay_id = scrapy.Field()
    title = scrapy.Field()
    #description = scrapy.Field()
    
    #product = scrapy.Field()
    price = scrapy.Field()
    bids = scrapy.Field()
    brand = scrapy.Field()
    #seller_id = scrapy.Field()
    year = scrapy.Field()
    era = scrapy.Field()
    franchise = scrapy.Field()
    character = scrapy.Field()
    toy_type = scrapy.Field()
    sell_date = scrapy.Field()
    size = scrapy.Field()
    gender = scrapy.Field()