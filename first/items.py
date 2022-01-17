# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FirstItem(scrapy.Item):
    # define the fields for your item here like:
    # new_title = scrapy.Field()
    # new_href = scrapy.Field()
    # time = scrapy.Field()
    add_all_anquangongcheng_trans = scrapy.Field()
    add_all_shuili_trans = scrapy.Field()
    add_all_gongshang_trans = scrapy.Field()
    add_all_ziranziyuan_trans = scrapy.Field()

class Gongshang_Item(scrapy.Item):
    title = scrapy.Field()
    time = scrapy.Field()
    url = scrapy.Field()
    lable = scrapy.Field()
    pass

class Shentai_Item(scrapy.Item):
    title = scrapy.Field()
    time = scrapy.Field()
    url = scrapy.Field()
    lable = scrapy.Field()
    pass

class Jidian_Item(scrapy.Item):
    title = scrapy.Field()
    time = scrapy.Field()
    url = scrapy.Field()
    lable = scrapy.Field()
    pass
