import scrapy
from scrapytutorial.items import QuoteItem
#QuotesSpider继承了scrapy的spider类
class QuotesSpider(scrapy.Spider):
    #每个项目唯一的名字，用来区分不同的spider
    name = "quotes"
    #允许爬取的域名
    allowed_domains = ["quotes.toscrape.com"]
    #包含了Spider在启动时候爬取的URL列表
    start_urls = ["https://quotes.toscrape.com/"]
    #parse负责解析返回的响应，提取数据或者进一步生成要处理的请求
    def parse(self, response):
        quotes = response.css('.quote')
        for quote in quotes:
            item = QuoteItem()
            item['text'] = quote.css('.text::text').extract_first()
            item['author'] = quote.css('.author::text').extract_first()
            item['tags'] = quote.css('.tags .tag::text').extract()
            yield item
        
        next = response.css('.pager .next a::attr("href")').extract_first()
        url = response.urljoin(next)
        yield scrapy.Request(url=url, callback=self.parse)
