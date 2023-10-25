import scrapy
from telegram import Bot

class JobinjaScrapySpider(scrapy.Spider):
    name = "jobinja_scrapy"
    allowed_domains = ["jobinja.ir"]
    start_urls = [
        "https://jobinja.ir/jobs?&filters%5Bkeywords%5D%5B0%5D=%20Flutter&filters%5Bkeywords%5D%5B0%5D=%20Flutter&preferred_before=1698235948&sort_by=published_at_desc"]

    async def parse(self, response, **kwargs):
        jobs = response.xpath(
            '//li[@class="o-listView__item o-listView__item--hasIndicator c-jobListView__item o-listView__item__application  "]')
        urls = []

        bot_token = '6546731453:AAHpSIiub7YWvRgGjBK8kOdkhkUcLCU4wrQ'
        bot = Bot(token=bot_token)
        chat_id = '398053047'

        for index, item in enumerate(jobs):
            text = item.xpath('//span[@class="c-jobListView__passedDays"]/text()').extract()[0]
            text = text.strip()
            print(text)
            if text == '(امروز)':
                url = \
                    jobs.xpath(
                        '//a[@class="o-listView__itemIndicator o-listView__itemIndicator--noPaddingBox"]/@href').extract()[
                        index]
                urls.append(url)

        print(len(urls))
        for x in urls:
            print('1')
            await bot.send_message(chat_id=chat_id, text=x)

        pass

