import scrapy

class HongloumengSpider(scrapy.Spider):
    name = "hongloumeng"
    start_urls = ["https://m.shicimingju.com/book/hongloumeng.html"]

    def parse(self, response):
        # 获取章节列表
        ch_list = response.xpath("//div[@class='list']/a")

        for ch in ch_list:
            ch_name = ch.xpath("text()").get()  # 获取章节名
            ch_url = response.urljoin(ch.xpath("@href").get())  # 获取完整链接

            print(f"正在爬取: {ch_name} - {ch_url}")

            # 进入详情页
            yield scrapy.Request(url=ch_url, callback=self.detail_page, meta={"ch_name": ch_name}, dont_filter=True)

    def detail_page(self, response):
        ch_name = response.meta["ch_name"]  # 获取章节名
        content = "\n".join(response.xpath("//div[@class='text p_pad']/p/text()").getall())  # 获取内容

        # 将章节内容传递给管道,scrapy也是异步爬取，章节混乱
        yield {
            "章节": ch_name,
            "内容": content
        }