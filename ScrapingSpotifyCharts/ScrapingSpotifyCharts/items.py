# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapingspotifychartsItem(scrapy.Item):
    # define the fields for your item here like:
    Author          = scrapy.Field()
    Colaborators   = scrapy.Field()
    Song         = scrapy.Field()
    ConcatName = scrapy.Field()
    List           = scrapy.Field()
    Ranking         = scrapy.Field()
    Link         = scrapy.Field()
