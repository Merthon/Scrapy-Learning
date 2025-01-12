import scrapy


class BookSpider(scrapy.Spider):
    name = "book"
    allowed_domains = ["antispider7.scrape.center"]
    start_urls = ["https://antispider7.scrape.center"]

    def parse(self, response):
        pass
