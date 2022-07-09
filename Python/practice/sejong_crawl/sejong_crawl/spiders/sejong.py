from cgi import parse_multipart
from this import d
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.responsetypes import Response
import re


def extractTextFromHTML(html: str):
    regex = r">\s*(.*?)\s*<"
    foundRegex = re.findall(regex, html)
    stripedRegex = map(lambda x: x.strip(), foundRegex)
    filteredRegex = filter(lambda x: len(x) != 0, stripedRegex)
    return " ".join(filteredRegex)


# '<span class="idx_wrap idx_place">일본국</span> <span class="idx_wrap idx_place">대마주 수호(對馬州守護)</span>'
class SejongSpider(CrawlSpider):
    name = "sejong"
    allowed_domains = ["sillok.history.go.kr"]
    start_urls = [
        "https://sillok.history.go.kr/id/kda_10009002_009",
        "https://sillok.history.go.kr/id/kda_10009002_008",
    ]
    rules = (
        Rule(
            LinkExtractor(
                allow=r"id/kda_1(0[0-9]|1[0-9]|2[0-9]|3[0-2])(0[1-9]|1[0-2])(0|1)(0[1-9]|1[0-9]|2[0-9]|30)_00[1-9]"
            ),
            callback="parse_item",
            follow=True,
        ),
    )

    def _parse_volume_date(self, response):
        path: str = '//*[@id="cont_area"]/div[1]/div[1]/div/span/text()'
        text = response.xpath(path).get()
        [volume_css, date_css] = text.strip().split(",")
        return volume_css.strip(), date_css.strip()

    def _parse_title(self, response):
        path: str = '//*[@id="cont_area"]/div[1]/div[1]/h3'
        title_html = response.xpath(path).get()
        return extractTextFromHTML(title_html)

    def _parse_hangul(self, response):
        path: str = "div.ins_left_in div.ins_view_pd .paragraph"
        title_html: list = response.css(path).getall()
        hangul_list = map(lambda html: extractTextFromHTML(html), title_html)
        return "\n\n".join(hangul_list)

    def _parse_hanza(self, response):
        path: str = '//*[@id="cont_area"]/div[1]/div[3]/div[2]/div/div/p'
        hanza_html: list = response.xpath(path).getall()
        hanza_list = map(lambda html: extractTextFromHTML(html), hanza_html)
        return "".join(hanza_list)

    def _parse_footnotes(self, response):
        path: str = ".ins_footnote li"
        footnotes_html: list = response.css(path)
        footnotes_list = map(
            lambda html: extractTextFromHTML(html.get()), footnotes_html
        )

    # [註 018]어명(御命) : 제령(制令).

    def parse_item(self, response):
        item = {}
        item["volume"], item["date"] = self._parse_volume_date(response)
        item["title"] = self._parse_title(response)
        item["hangul"] = self._parse_hangul(response)
        item["hanza"] = self._parse_hanza(response)

        return item
