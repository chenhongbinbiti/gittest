import scrapy
class Qiubai(scrapy.Spider):
    name = "qiubai"
    start_url = ["http://qiushibaike.com",]
    def parse(self, response):
        print response.xpath('//div[@class="content"]').extract()

