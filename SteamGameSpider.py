import scrapy
import re
from urllib.parse import urlencode
from urllib.parse import urlparse
from spider_steam.items import SpiderSteamItem

pages = [i for i in range(1, 3)]
queries = ['sims', 'casual', 'simulation']


def platform_clean(dirty_string):
    cleaning = re.findall(" \w+\"", dirty_string)
    cleaning = re.findall("\w+", cleaning[0])
    return cleaning[0]



class SteamgamespiderSpider(scrapy.Spider):
    name = 'SteamGameSpider'

    def start_requests(self):
        global page
        for query in queries:
            for page in pages:
                url = 'https://store.steampowered.com/search/?' + urlencode({'term': query, 'page': str(page)})
                yield scrapy.Request(url=url, callback=self.parse_keyword_response)

    def parse_keyword_response(self, response):
        games = set()
        for res in response.xpath('//div[contains(@id, "search_resultsRows")]/a/@href').extract():
            games.add(res)

        for game in games:
            yield scrapy.Request(url=game, callback=self.parse)

        url = urlparse(response.url[-1]) + str(page)
        yield scrapy.Request(url=url, callback=self.parse_keyword_response)

    def parse(self, response):
        item = SpiderSteamItem()
        game_name = response.xpath('//div[contains(@class,"apphub_AppName")]/text()').extract()
        game_category = response.xpath('//div[contains(@class,"blockbg")]/a[2]/text()').extract()
        game_rating_count = response.xpath(
            '//div[@class="user_reviews"]/div[@itemprop="aggregateRating"]//span[contains(@class,"responsive_hidden")]/text()').extract()
        game_score = response.xpath('//span[contains(@class,"game_review_summary positive")]/text()').extract()
        game_release_date = response.xpath('//div[contains(@class, "release_date")]/div[2]/text()').extract()
        game_creator = response.xpath('//div[@id="developers_list"]/a/text()').extract()
        game_tags = response.xpath('//div[contains(@class,"glance_tags popular_tags")]/a/text()').extract()
        game_price = response.xpath('//div[contains(@class ,"discount_final_price")]/text()').extract()
        game_platforms = response.xpath('//div[contains(@class, "game_area_purchase_platform")]/span').extract()

        if len(game_name) != 0:
            item['game_name'] = ''.join(game_name[0]).strip()

        item['game_category'] = ''.join(game_category).strip()
        item['game_rating_count'] = ''.join(game_rating_count).strip()
        item['game_rating_count'] = item['game_rating_count'][1:item['game_rating_count'].find(')')]

        if len(game_score) != 0:
            item['game_score'] = ''.join(game_score[0]).strip()

        item['game_release_date'] = ''.join(game_release_date).strip()
        item['game_creator'] = ''.join(game_creator).strip()
        item['game_tags'] = ''.join(game_tags).strip().split()
        item['game_price'] = ''.join(game_price).strip()

        if item['game_price'] != '':
            item['game_price'] = item['game_price'][:item['game_price'].find(' ')] + ' RUB'

        item['game_platforms'] = sorted(list(
            set(map(lambda x: platform_clean(x), game_platforms))),
            reverse=True)
        yield item
