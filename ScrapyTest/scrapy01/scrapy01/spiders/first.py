import scrapy


class FirstSpider(scrapy.Spider):
    name = 'first'
    #允许的域名：限定url列表中哪些允许访问
    # allowed_domains = ['www.baidu.com']
    #起始的url列表
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        #  解析作者名称以及段子内容
        div_list = response.xpath('//*[@id="content"]/div/div[2]/div')
        for div in div_list:
            #  extract将Selector对象中的data参数提取出来
            #  列表调用extract，将列表中所有Selector对象中的data参数提取出来
            author = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
            content = div.xpath('./a[1]/div/span//text()').extract()
            content = ''.join(content)
            print(author)
            print(content)
