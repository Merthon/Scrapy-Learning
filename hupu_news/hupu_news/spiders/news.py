import scrapy


class NewsSpider(scrapy.Spider):
    name = "news"
    allowed_domains = ["soccer.hupu.com"]
    start_urls = ["https://soccer.hupu.com/"]
    
    def start_requests(self):
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
        }
        for url in self.start_urls:
            yield scrapy.Request(url, headers=headers, callback=self.parse)
    # parse方法用来解析响应内容，抓取每个新闻标题和链接
    def parse(self, response):
        for article in response.xpath('/html/body/div/div/main/div[1]/div[2]//a'):
            title = article.xpath('.//text()').get()
            link = article.xpath('.//@href').get()

            if title and link:  # 确保有提取到标题和链接
                yield {
                    'title': title,
                    'link': response.urljoin(link),  # 获取完整链接
                }
# /html/body/div/div/main/div[1]/div[2]