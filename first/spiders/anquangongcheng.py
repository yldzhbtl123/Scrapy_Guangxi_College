import re

import scrapy
from first.items import FirstItem
from first.spiders.tuple_to_list import tuple_to_list

class AnquangongchengSpider(scrapy.Spider):
    name = 'anquangongcheng'
    # allowed_domains = ['https://www.gxaqzy.cn/']
    start_urls = ['https://www.gxaqzy.cn/xwzx/tzgg']
    custom_settings = {'ITEM_PIPELINES':{'first.pipelines.AnquangongchengPipeline': 300}}

    page_num = 2


    def parse(self, response):
        new_title = []
        new_href =[]
        title_list = response.xpath('//*[@id="content"]/div/div/div[2]/ul//a/text()').extract()
        time = response.xpath('//*[@id="content"]//li/span[@class="date"]/text()').extract()
        href = response.xpath('//*[@id="content"]//ul[@class="newsList"]//a/@href').extract()
        lable = '广西安全工程职业技术学院'
        for i in href:
            if 'https://www.gxaqzy.cn/' not in i:
                i = 'https://www.gxaqzy.cn/'+ i
                new_href.append(i)
            else:
                new_href.append(i)

        add_all_anquangongcheng = list(zip(title_list,time,new_href))
        add_all_anquangongcheng_trans = tuple_to_list().tuple_to_list(add_all_anquangongcheng)
        for i in range(len(add_all_anquangongcheng_trans)):
            add_all_anquangongcheng_trans[i].append(lable)

        # print(add_all)


        # for title_name in title_list:
        #     re_ch_and_number = re.compile(r'\S+')
        #     l = ''.join(re_ch_and_number.findall(title_name))
        #     re_ch_and_number2=re.search(r'\S*\B招聘\B\S*', l)
        #     if re_ch_and_number2:
        #         n2 = re_ch_and_number2.group()
        #         new_title .append(n2)
        # # print(new_title)
        # print(add_all)
        add_all_anquangongcheng_trans = [list(i) for i in add_all_anquangongcheng_trans]
        for i in add_all_anquangongcheng_trans[::-1]:
            if "招聘" not in i[0]:
                add_all_anquangongcheng_trans.remove(i)

        #
        # print('++++++++++++++++++++++++++++++++++')

        for title_name in add_all_anquangongcheng_trans:
            re_ch_and_number = re.compile(r'\S+')
            l = ''.join(re_ch_and_number.findall(title_name[0]))
            title_name[0] = l

        item = FirstItem()
        item['add_all_anquangongcheng_trans']= add_all_anquangongcheng_trans
        # item['new_href'] = new_href
        # item['time'] = time

        yield item


        while self.page_num < 4:
            new_url = f'https://www.gxaqzy.cn/xwzx/tzgg_{self.page_num}'
            self.page_num += 1
            yield scrapy.Request(url=new_url,callback=self.parse)






