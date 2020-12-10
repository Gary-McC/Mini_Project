# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 15:11:53 2020

@author: Annoy
"""
import scrapy
import json
class QuotesSpider(scrapy.Spider):
    name = "xpath"
    start_urls = [
        'http://quotes.toscrape.com/page/1/']

    def parse(self, response):
        for stuff in response.xpath('//div[@class="quote"]'):
            filename=(
                'C:\\Users\\Annoy\\Desktop\\Spyder\\Test\\Example\\Example\\spiders\\xpath-scraper-results.json'
                )
            data=json.dumps({
                    'text': stuff.xpath('./span[@class="text"]/text()').get(),
                    'author': stuff.xpath('.//small[@class="author"]/text()').get(),
                    'tags': stuff.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').getall()
                })
            with open(filename,'a') as f:
                f.write(data)
        next_page = response.xpath('//li[@class="next"]/a/@href').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)