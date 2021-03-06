import scrapy

class BrickSetSpider(scrapy.Spider):
    name = "bricketset_spider"
    start_urls = ['http://brickset.com/sets/year-2020']
    