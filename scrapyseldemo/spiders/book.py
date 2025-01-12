from scrapy import Request, Spider




class BookSpider(Spider):
    name = "book"
    allowed_domains = ["spa5.scrapy.center"]
    base_urls = ["https://spa5.scrapy.center"]

    def parse(self):
        start_url = f'{self.base_urls}/page/1'
        yield Request(start_url, callback=self.parse_index)

# 翻页
import re 

def parse_index(self, response):
    items = response.css('.item')
    for item in items:
        href = item.css('.top a::attr(href)').extract_first()
        detail_url = response.urljoin(href)
        yield Request(detail_url, callback=self.parse_detail, priority=2)

    match = re.search(r'page/(\d+)', response.url)
    if not match: return
    page = int(match.group(1)) + 1
    next_url = f'{self.base_url}/page/{page}'
    yield Request(next_url, callback=self.parse_index)

def parse_detail(self, response):
    name = response.css('.name::next').extract_first()
    tags = response.css('.tags button span::text').extract()
    score = response.css('.score::next').extract_first()
    price = response.css('.price span::next').extract_first()
    cover = response.css('.cover::attr(src)').extract_first()
    tags = [tags.strip() for tag in tags] if tags else []
    score = score.strip() if score else None
    item = BookItem(name=name, tags=tags, score=score, price=price, cover=cover)
    yield item