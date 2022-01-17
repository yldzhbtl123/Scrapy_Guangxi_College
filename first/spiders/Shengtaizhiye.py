import scrapy
import re
import time
from first.items import Shentai_Item
from first.spiders.tuple_to_list import tuple_to_list

class ShengtaizhiyeSpider(scrapy.Spider):
    name = 'Shengtaizhiye'
    # allowed_domains = ['www.gxstzy.cn']
    start_urls = ['https://www.gxstzy.cn/tzxw/tzgg.htm']
    custom_settings = {'ITEM_PIPELINES': {'first.pipelines.ShengtaizhiyePipeline': 301}}
    page_num = 65


    def parse(self,response):
        max_page = int(response.xpath('//span[@class="p_pages"]/span[9]/a/text()').extract_first())
        while self.page_num < max_page:
            new_url = f'https://www.gxstzy.cn/tzxw/tzgg/{self.page_num}.htm'
            self.page_num += 1
            yield scrapy.Request(url=new_url,callback=self.parse1)
        else:
            new_url = f'https://www.gxstzy.cn/tzxw/tzgg.htm'
            yield scrapy.Request(url=new_url, callback=self.parse1)

    def parse1(self, response):
        href2=[]
        href = response.xpath('//div[@class="list_right fl"]/ul/li/a/@href').extract()
        for h in href:
            if ".." or "../.." in h:
                h2 = h.strip("../")
                h3 = 'https://www.gxstzy.cn/' + h2
                href2.append(h3)
        for url1 in href2:
            item = Shentai_Item()
            item['url'] = url1
            yield scrapy.Request(url=url1, callback=self.parse_new_detail,meta={'item':item})

    def parse_new_detail(self,response):
        title = response.xpath('//div[@class="content"]//h2/text()').extract_first()
        time_1 = response.xpath('//div[@class="ly"]/p/text()').extract_first()
        pattern = re.compile(r'(([0-9]{3}[1-9]|[0-9]{2}[1-9][0-9]|[0-9][1-9][0-9]{2}|[1-9][0-9]{3})-(((0[13578]|1[02])-(0[1-9]|[12][0-9]|3[01]))|((0[469]|11)-(0[1-9]|[12][0-9]|30))|(02-(0[1-9]|[1][0-9]|2[0-8]))))|((([0-9]{2})(0[48]|[2468][048]|[13579][26])|((0[48]|[2468][048]|[3579][26])00))-02-29)')
        time = pattern.search(str(time_1)).group()
        lable = "广西生态工程职业技术学院"

        item = response.meta['item']
        item['title'] = title
        item['time'] = time
        item['lable'] = lable

        yield item

















