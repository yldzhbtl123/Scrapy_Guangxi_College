import scrapy
from first.items import FirstItem

from first.spiders.tuple_to_list import tuple_to_list


class ShuilidianliSpider(scrapy.Spider):
    name = 'Shuilidianli'
    # allowed_domains = ['http://www.gxsdxy.cn/']
    start_urls = ['http://www.gxsdxy.cn/pagelist/28/249']
    custom_settings = {'ITEM_PIPELINES':{'first.pipelines.ShuilidianliPipeline': 300}}

    def parse(self, response):
        new_href =[]
        title_list = response.xpath('//*[@id="width1200"]//table[@class="views-table cols-0 table table-0 table-0 table-0 table-0"]//tr/td[1]//a/text()').extract()
        time = response.xpath('//*[@id="width1200"]//table[@class="views-table cols-0 table table-0 table-0 table-0 table-0"]//tr/td[2]//span[@class="date-display-single"]/text()').extract()
        href = response.xpath('//*[@id="width1200"]//table[@class="views-table cols-0 table table-0 table-0 table-0 table-0"]//tr/td[1]//a/@href').extract()
        lable = "广西水利电力职业技术学院"
        for i in href:
            if 'http://www.gxsdxy.cn' not in i:
                i = 'http://www.gxsdxy.cn'+ i
                new_href.append(i)

            else:
                new_href.append(i)


        add_all_shuili = list(zip(new_href,title_list,time))
        add_all_shuili_trans = tuple_to_list().tuple_to_list(add_all_shuili)
        for i in range(len(add_all_shuili_trans)):
            add_all_shuili_trans[i].append(lable)


        item = FirstItem()
        item['add_all_shuili_trans']= add_all_shuili_trans
        yield item


