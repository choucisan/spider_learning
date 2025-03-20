# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapyPipeline:
    def open_spider(self, spider):
        # 打开文件进行写入
        self.file = open('hongloumeng.txt', 'a', encoding='utf-8')

    def close_spider(self, spider):
        # 关闭文件
        self.file.close()

    def process_item(self, item, spider):
        # 将每个章节内容写入文本文件
        self.file.write(f"章节: {item['章节']}\n")
        self.file.write(f"内容: {item['内容']}\n\n")
        return item
