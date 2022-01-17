import scrapy
from first.items import Gongshang_Item
from first.spiders.tuple_to_list import tuple_to_list
import re

class GongshangSpider(scrapy.Spider):
    name = 'Gongshang'
    # allowed_domains = ['www.gxgsxy.com']
    start_urls = ['http://www.gxgsxy.com/public/news/zbzp/']
    custom_settings = {'ITEM_PIPELINES': {'first.pipelines.GongshangPipeline': 301}}


    def parse(self, response):
        pattern = re.compile(r'(\d+){2}')
        dump  = response.xpath('//*[@class="pagecss"]/a[1]/@href').extract_first()
        print(dump)
        page_num = int(pattern.search(str(dump)).group())
        print(type(page_num))

        while page_num > 8:
            new_url = f'http://www.gxgsxy.com/public/news/zbzp/List_{page_num}.html'
            page_num -= 1
            yield scrapy.Request(url=new_url, callback=self.parse_request)

    def parse_request(self, response):
        new_href = []
        href = response.xpath('//*[@id="subleft"]/div[@class="newslist"]/ul/li/a/@href').extract()
        for i in href:
            if 'http://www.gxgsxy.com/' not in i:
                i = 'http://www.gxgsxy.com/' + i
                new_href.append(i)
            else:
                new_href.append(i)

        for url1 in new_href:
            item = Gongshang_Item()
            item['url'] = url1
            yield scrapy.Request(url=url1, callback=self.parse_new_detail, meta={'item': item})

    def parse_new_detail(self, response):
        title = response.xpath('//*[@id="subcontent1"]/h3/text()').extract_first()
        time = response.xpath('//*[@id="info"]/text()[3]').extract()
        pattern = re.compile(r'(\d{4}|\d{2})(年)((1[0-2])|(0?[1-9]))(月)(([12][0-9])|(3[01])|(0?[1-9]))(日)')
        str1 = time
        str_new = pattern.search(str(str1)).group()
        time_rep = str_new.replace('年', '-').replace('月', '-').replace('日', '')
        lable = '广西工商职业技术学院'

        item = response.meta['item']
        item['title'] = title
        item['time'] = time_rep
        item['lable'] = lable

        yield item







