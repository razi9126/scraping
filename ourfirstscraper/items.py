# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class OurfirstscraperItem(scrapy.Item):
    # define the fields for your item here like:
    titles = scrapy.Field()
    votes = scrapy.Field()
    comments = scrapy.Field()

