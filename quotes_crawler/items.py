# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst, MapCompose, Join
from w3lib.html import remove_tags

def remove_unicodes(value : str) -> str:
    return value.replace("\u201c", '').replace("\u201d", '').replace("\u2018", "'").replace("\u2019", "'")

def get_image_name(value : str) -> str:
    return value.split('/')[-1]

def list_to_comma_str(values : list) -> str:
    return ",".join(values)

class QuotesItem(scrapy.Item):
    # define the fields for your item here like:
    quote_text = scrapy.Field(
        input_processor=MapCompose(remove_tags, remove_unicodes, str.strip),
        output_processor=TakeFirst()
    )
    author = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip),
        output_processor=TakeFirst()
    )
    img = scrapy.Field(
        input_processor=MapCompose(get_image_name),
        output_processor=TakeFirst()
    )
    tags = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=Join(',')
    )