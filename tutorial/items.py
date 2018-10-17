# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    srcInfo = scrapy.Field()
    click_rate = scrapy.Field()
    url = scrapy.Field()
    from_type = scrapy.Field()
    ctime = scrapy.Field()
    item = scrapy.Field()
    content = scrapy.Field()
    contents = scrapy.Field()
    release_time = scrapy.Field()
    source = scrapy.Field()
    date = scrapy.Field()
    time = scrapy.Field()
    top_img_url = scrapy.Field()
    img_num = scrapy.Field()
    pass
