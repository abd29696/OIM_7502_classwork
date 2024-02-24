# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SlickchartsItem(scrapy.Item):

    number = scrapy.Field()
    company = scrapy.Field()
    symbol = scrapy.Field()
    ytd_return = scrapy.Field()



