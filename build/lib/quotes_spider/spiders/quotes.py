import json

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com']

    def parse(self, response, **kwargs):
        quotes = response.xpath('//div[@class="quote"]')

        s = []

        for index, item in enumerate(quotes):
            text = item.xpath('//span[@class="text"]/text()').extract()[0]
            auther_name = item.xpath('//small[@class="author"]/text()').extract()[0]
            link_about = 'https://quotes.toscrape.com' + item.xpath('//span/a/@href').extract()[0]

            yield {
                'text': text,
                'auther_name': auther_name,
                'link_about': link_about
            }

        url = response.xpath('//*[@class="next"]/a/@href').extract_first()

        url = response.urljoin(url)

        print(url)

        yield scrapy.Request(url)
