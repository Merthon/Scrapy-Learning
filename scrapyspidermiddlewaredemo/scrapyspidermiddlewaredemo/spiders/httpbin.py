from scrapy import Spider, Request

class HttpbinSpider(Spider):
    name = "httpbin"
    allowed_domains = ["www.httpbin.org"]
    start_url = 'https://www.httpbin.org/get'

    def start_request(self):
        for i in range(5):
            url = f'{self.start_url}?query={i}'
            yield Request(url, callback=self.parse)

    def parse(self, response):
        print(response.text)