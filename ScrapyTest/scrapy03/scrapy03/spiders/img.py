import scrapy
from scrapy03.items import Scrapy03Item

class ImgSpider(scrapy.Spider):
    name = 'img'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://sc.chinaz.com/tupian/']

    def parse(self, response):
        div_list = response.xpath('//*[@id="container"]/div')
        for div in div_list:
            src = div.xpath('./div/a/img/@src2').extract_first()

            item = Scrapy03Item()
            item['src'] = src

            yield item
