# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from itemadapter import ItemAdapter
import json


class SpiderSteamPipeline:
    def open_spider(self, spider):
        self.file = open("items.json", "w")
        self.file.write('[')

    def close_spider(self, spider):
        self.file.write(']')
        self.file.close()

    def process_item(self, item, spider):
        if item["game_release_date"][-4:] >= "2000":
            line = json.dumps(ItemAdapter(item).asdict(), indent=9, ensure_ascii=False) + ',' + '\n'
            self.file.write(line)
        return item
