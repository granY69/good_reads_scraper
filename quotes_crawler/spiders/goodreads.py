import scrapy
from scrapy.loader import ItemLoader
from quotes_crawler.items import QuotesItem
from scrapy.shell import inspect_response

class GoodreadsSpider(scrapy.Spider):
    name = 'goodreads'
    allowed_domains = ['goodreads.com']
    start_urls = ['https://www.goodreads.com/quotes?page=1']

    def parse(self, response):
        quotes = response.css("div.quote")
        for quote in quotes:
            loader = ItemLoader(item=QuotesItem(), selector=quote, response=response)
            loader.add_css('quote_text', "div.quoteText::text")
            loader.add_css('author', "span.authorOrTitle::text")
            loader.add_css('img', "img::attr(src)")
            loader.add_css('tags', "div.greyText a::text")
            yield loader.load_item()
        # inspect_response(response, self)
