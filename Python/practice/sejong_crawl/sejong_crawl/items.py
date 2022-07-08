# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SejongCrawlItem(scrapy.Item):
    volume = scrapy.Field()  # 세종실록 1권
    date = scrapy.Field()  # 세종 즉위년 8월 11일 무자 1번째기사

    title = scrapy.Field()  # (optional) 근정전에서 즉위 교서를 반포하다
    hangul = scrapy.Field()
    # footnotes = scrapy.Field()  # 한글 주석, [註 162]전조(前朝) : 고려.
    hanza = scrapy.Field()

    pass
