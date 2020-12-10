# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 14:49:28 2020

@author: Annoy
"""
import scrapy
import json
class QuotesSpider(scrapy.Spider):
    name = "css"
    start_urls = [
        'http://quotes.toscrape.com/page/1/']

    def parse(self, response):
        for quote in response.css('div.quote'):
            filename=(
                'C:\\Users\\Annoy\\Desktop\\Spyder\\Test\\Example\\Example\\spiders\\css-scraper-results.json'
                )
            data=json.dumps({
                    'text': quote.css('span.text::text').get(),
                    'author': quote.css('small.author::text').get(),
                    'tags': quote.css('div.tags a.tag::text').getall()
                })
            with open(filename,'a') as f:
                f.write(data)
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)