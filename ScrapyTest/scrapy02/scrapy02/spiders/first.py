import scrapy
from ScrapyTest.scrapy02.scrapy02.items import Scrapy02Item


class FirstSpider(scrapy.Spider):
    name = 'first'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.zhipin.com/job_detail/?query=python']

    url = 'https://www.zhipin.com/job_detail/?query=python&page=%d'
    page_num = 2
    def parse_detail(self, response):
        item = response.meta['item']
        job_desc = response.xpath('//*[@id="main"]/div[3]/div/div[2]/div[2]/div[1]/div//text()').extract()
        job_desc = ''.join(job_desc)
        item['job_desc'] = job_desc

        yield item

    def parse(self, response):
        li_list = response.xpath('//*[@id="main"]/div/div[2]/ul/li')
        for li in li_list:
            job_name = li.xpath('.//div[@class="job-title"]/span[1]/a/text()').extract_first()
            item = Scrapy02Item()
            item['job_name'] = job_name
            detail_url = 'https://www.zhipin.com' + li.xpath('.//div[@class="job-title"]/span[1]/a/@href').extract_first()

            yield scrapy.Request(detail_url, callable=self.parse_detail, meta={'item': item})
        if self.page_num <= 3:
            new_url = format(self.url,self.page_num)
            self.page_num += 1

            yield scrapy.Request(new_url, callback=self.parse)
