import scrapy
from kcrawler.items import KcrawlerItem


class MainSpider(scrapy.Spider):
    name = 'mainspider'

    def __init__(self, keyword=None, *args, **kwargs):
        super(MainSpider, self).__init__(*args, **kwargs)
        self.start_urls = [
            'https://vijaykarnataka.indiatimes.com/topics/%s' % keyword]

    def parse(self, response):
        item = KcrawlerItem()
        filename = 'response.json'
        item["content"] = []
        listofarticles = response.css(
            'div.tab_content div.content span.title::text').getall()
        for i in listofarticles:
            self.log(i)
            item["content"].append(i)
        self.log("Saved file %s" % filename)
        yield item
