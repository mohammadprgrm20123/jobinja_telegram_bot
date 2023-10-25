import scrapy


class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["exapmle.com"]
    start_urls = ["https://exapmle.com"]

    def parse(self, response):
        pass
