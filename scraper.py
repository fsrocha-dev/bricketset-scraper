import scrapy

class QuotesSpider(scrapy.Spider):
    name = "brickset"
    start_urls = ['http://quotes.toscrape.com']
    
    def parse(self, response):
        SET_SELECTOR = '.quote'
        for quote in response.css(SET_SELECTOR):
            TEXT_SELECTOR = 'span ::text'
            AUTHOR_SELECTOR = 'span small ::text'
            yield {
                'text': quote.css(TEXT_SELECTOR).extract_first(),
                'Author': quote.css(AUTHOR_SELECTOR).extract_first(),
            }