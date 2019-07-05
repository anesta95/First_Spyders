import scrapy
from scrapy.crawler import CrawlerProcess


class MySpider(scrapy.Spider):
    name = 'MySpider'

    def start_requests(self):
        yield scrapy.Request(url='https://www.datacamp.com',
                             callback=self.parse)

    def parse(self, response):
        crs_titles = response.xpath('''//h4[contains(@class, "block__title")] /
                                    text()''')
        crs_desrs = response.xpath('''//
                                  p[contains(@class,"block__description")] /
                                  text()''')
        for crs_title, crs_desr in zip(crs_titles, crs_desrs):
            dc_dict[crs_titles] = crs_desrs


dc_dict = dict()


process = CrawlerProcess()
process.crawl(MySpider)
process.start()

print(dc_dict)
