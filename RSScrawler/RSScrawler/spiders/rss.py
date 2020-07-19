import scrapy
from scrapy.item import Item, Field
from scrapy.loader.processors import TakeFirst, MapCompose, Join
from w3lib.html import remove_tags, replace_entities, replace_escape_chars
from scrapy.loader import ItemLoader



class newsItem(Item):
    description = Field(
        input_processor = MapCompose(remove_tags, replace_entities,
                                    replace_escape_chars,str.strip),
                                    
        output_processor = Join()
    )

class SomeSpider(scrapy.Spider):
    name = 'rss'
    start_urls = ['https://news.google.com/rss?hl=zh-TW&gl=TW&ceid=TW:zh-Hant']

    def parse(self, response):

        with open("../../Q1/news.rss","wb") as f:
            f.write(response.body)
        
        posts = response.xpath("//channel/item")


        for p in posts:
            item = newsItem()
            il = ItemLoader(item=item, response=response)

            description = p.xpath("description/text()").extract()
            il.add_value("description",description)
            item = il.load_item()

            yield item