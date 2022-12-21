# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderSteamItem(scrapy.Item):
    game_name = scrapy.Field()
    game_category = scrapy.Field()
    game_rating_count = scrapy.Field()
    game_score = scrapy.Field()
    game_release_date = scrapy.Field()
    game_creator = scrapy.Field()
    game_tags = scrapy.Field()
    game_price = scrapy.Field()
    game_platforms = scrapy.Field()

