import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy05.items import SunItem,DetailItem

class SunSpider(CrawlSpider):
    name = 'sun'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://wz.sun0769.com/political/index/politicsNewest']

    Link_detail = LinkExtractor(allow=r'/political/politics/index\?id=\d+')
    rules = (
        #  规则解析器
        Rule(LinkExtractor(allow=r'id=1&page=\d+'), callback='parse_item', follow=True),
        Rule(Link_detail, callback='parse_detail', follow=False)
    )

    def parse_item(self, response):
        li_list = response.xpath('/html/body/div[2]/div[3]/ul[2]/li')
        for li in li_list:
            li_num = li.xpath('./span[1]/text()').extract_first()
            li_title = li.xpath('./span[3]/a/text()').extract_first()
            item = SunItem()
            item['li_num'] = li_num
            item['li_title'] = li_title

            yield item
        # item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item

    def parse_detail(self, response):
        new_id = response.xpath('/html/body/div[3]/div[2]/div[2]/div[1]/span[4]/text()').extract_first()
        new_content = response.xpath('/html/body/div[3]/div[2]/div[2]/div[2]/pre/text()').extract_first()
        item = DetailItem()
        item['new_id'] = new_id
        item['new_content'] = new_content

        yield item
