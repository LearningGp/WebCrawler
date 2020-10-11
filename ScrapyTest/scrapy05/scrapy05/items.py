# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SunItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    li_num = scrapy.Field()
    li_title = scrapy.Field()


class DetailItem(scrapy.Item):
    new_id = scrapy.Field()
    new_content = scrapy.Field()

