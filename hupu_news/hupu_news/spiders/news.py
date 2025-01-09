import scrapy
import pymongo


class NewsSpider(scrapy.Spider):
    name = "news"
    allowed_domains = ["soccer.hupu.com"]
    start_urls = ["https://soccer.hupu.com/"]

    # 添加数据库
    def __init__(self, *args, **kwargs):
        super(NewsSpider, self).__init__(*args, **kwargs)
        # 连接到 MongoDB 数据库
        self.client = pymongo.MongoClient("mongodb://admin:admin@localhost:27017/")  # 默认本地 MongoDB
        self.db = self.client["test"]  # 数据库名称
        self.collection = self.db["news"]  # 集合名称
    
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
    def insert_to_db(self, title, link):
        # 插入新闻数据到 MongoDB
        data = {"title": title, "link": link}
        self.collection.insert_one(data)  # 插入单条数据
        self.log(f"Inserted news: {title}")