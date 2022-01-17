import re

import scrapy
from first.items import Jidian_Item
class JidianSpider(scrapy.Spider):
    name = 'Jidian'
    # allowed_domains = ['http://www.gxcme.edu.cn/']
    start_urls = ['http://www.gxcme.edu.cn/z/p-1.html']
    custom_settings = {'ITEM_PIPELINES': {'first.pipelines.JidianPipeline': 301}}
    page_num = 1

    def parse(self, response):
        while self.page_num < 4:
            new_url = f'http://www.gxcme.edu.cn/z/p-{self.page_num}.html'
            self.page_num += 1
            yield scrapy.Request(url=new_url, callback=self.parse1)

    def parse1(self, response):
        href = response.xpath('//*[@id="list"]/li/a/@href').extract()
        for url1 in href:
            item = Jidian_Item()
            item['url'] = url1
            yield scrapy.Request(url=url1, callback=self.parse_new_detail,meta={'item':item})

    def parse_new_detail(self, response):
        title = response.xpath('//*[@id="notice2txtArea"]/h3/text()').extract_first()
        time_1 = response.xpath('//*[@id="notice2txtArea"]/p[2]/text()').extract_first()
        pattern = re.compile(
            r'(([0-9]{3}[1-9]|[0-9]{2}[1-9][0-9]|[0-9][1-9][0-9]{2}|[1-9][0-9]{3})-(((0[13578]|1[02])-(0[1-9]|[12][0-9]|3[01]))|((0[469]|11)-(0[1-9]|[12][0-9]|30))|(02-(0[1-9]|[1][0-9]|2[0-8]))))|((([0-9]{2})(0[48]|[2468][048]|[13579][26])|((0[48]|[2468][048]|[3579][26])00))-02-29)')
        time = pattern.search(str(time_1)).group()
        lable = "广西机电职业技术学院"

        item = response.meta['item']
        item['title'] = title
        item['time'] = time
        item['lable'] = lable

        yield item
