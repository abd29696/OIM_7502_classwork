import scrapy
from slickcharts.items import SlickchartsItem


class SlickchartsscrapperSpider(scrapy.Spider):
    name = "slickchartsscrapper"
    allowed_domains = ["www.slickcharts.com"]
    start_urls = ["https://www.slickcharts.com/sp500/performance"]

    def parse(self, response):
        slickcharts = SlickchartsItem()
        rows = response.xpath('//tbody/tr')

        for row in rows:

            slickcharts['number'] = row.xpath('td[1]/text()').get()

            slickcharts['company'] = row.xpath('td[2]/a/text()').get()

            slickcharts['symbol'] = row.xpath('td[3]/a/text()').get()

            ytd_return_raw = row.xpath('td[4]/text()').get()
            slickcharts['ytd_return'] = ytd_return_raw.replace(u'\xa0', '')

            yield slickcharts
