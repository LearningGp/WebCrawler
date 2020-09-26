# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class Scrapy01Pipeline:
    #  处理item对象，每接收一次调用一次
    fp = None
    #  重写父类方法

    def open_spider(self, spider):
        print('start')
        self.fp = open('./qiubai.txt', 'w', encoding='utf-8')

    def process_item(self, item,  spider):
        author = item['author']
        content = item['content']
        self.fp.write(author+':'+content+'\n')
        return item

    def close_spider(self, spider):
        print('over')
        self.fp.close()
