import scrapy
import re

class SvetnewparsSpider(scrapy.Spider):
    name = "svetnewpars"
    allowed_domains = ["https://xn--b1ag8ag.xn--80asehdb/catalog/lyustry"]
    start_urls = ["https://xn--b1ag8ag.xn--80asehdb/catalog/potolochnie-lyustry"]

    def parse(self, response):
        svets = response.css('div.col-xs-6')
        for svet in svets:
            yield {
                'name': svet.css('div.product-item-title a::text').get(),
                'price': re.sub('\D', '',svet.css('div.product-item-price-container span::text')[1].get()),
                'url': svet.css('a').attrib['href']
            }

