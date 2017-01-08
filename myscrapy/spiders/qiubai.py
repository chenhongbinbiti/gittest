import scrapy
class Qiubai(scrapy.Spider):
    name = "qiubai"
    start_url = ["http://www.qiushibaike.com",]
    def parse(self, response):
        print response.xpath('//div[@class="content"]').extract()

