from scrapy import Field, Item

class BookItem(Item):
    authors = Field()
    catalog = Field()
    comment = Field()
    cover = Field()
    id = Field()
    introduction = Field()
    isbn = Field()
    name = Field()
    page_number = Field()
    price = Field()
    publish_at = Field()
    publisher = Field()
    score = Field()
    tags = Field()
    translators = Field()