import scrapy
# from adcb_uae_sub_copy.items import Product
from lxml import html

class Adcb_uae_sub_copySpider(scrapy.Spider):
    name = "adcb_uae_sub_copy"
    start_urls = ["https://example.com"]

    def parse(self, response):
        parser = html.fromstring(response.text)
        print("Visited:", response.url)
