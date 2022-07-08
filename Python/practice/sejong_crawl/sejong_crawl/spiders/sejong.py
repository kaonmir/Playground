import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.responsetypes import Response
import re


def extractTextFromHTML(html: str):
    regex = r">(.*?)<"
    return ''.join(re.findall(regex, html))


class SejongSpider(CrawlSpider):
    name = 'sejong'
    allowed_domains = ['sillok.history.go.kr']
    start_urls = [
        'https://sillok.history.go.kr/id/kda_10008014_002'
    ]
# 1 31 04 0  03 _002
# 1 년 월 윤년 일  기사

# 년 : 00 ~ 32

    rules = (
        Rule(LinkExtractor(
            allow=r'id/kda_1(0[0-9]|1[0-9]|2[0-9]|3[0-2])(0[1-9]|1[0-2])(0|1)(0[1-9]|1[0-9]|2[0-9]|30)_00[1-9]'),
            callback='parse_item',
            follow=True),
    )

    def parse_item(self, response):
        item = {}

        # hangul
        hangul_css: list = response.css(
            'div.ins_left_in div.ins_view_pd .paragraph').getall()
        hangul_list = map(lambda html: extractTextFromHTML(html), hangul_css)

        item['hangul'] = '\n\n'.join(hangul_list)

        # title
        title_css = response.xpath(
            '//*[@id="cont_area"]/div[1]/div[1]/h3').get()
        item['title'] = extractTextFromHTML(title_css)

        return item


# In [10]: response.css("div.ins_left_in div.ins_view_pd .paragraph::text").getall()
