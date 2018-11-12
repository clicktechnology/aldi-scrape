# -*- coding: utf-8 -*-
import scrapy
import json

class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['aldi.co.uk']
    base_url = "https://www.aldi.co.uk/c/groceries/groceriescategories?sort=name-asc&q=%3Aname-asc%3AtransactionalStatus%3Atransactional%3AtransactionalStatus%3Anontransactional"
    start_urls = [
        'https://www.aldi.co.uk/c/groceries/groceriescategories?sort=name-asc&q=%3Aname-asc%3AtransactionalStatus%3Atransactional%3AtransactionalStatus%3Anontransactional'
        ]
    for i in range(1, 100):
        start_urls.append(base_url + "&page=" + str(i))

    def parse(self, response):
        my_json = response.xpath('//*[@class="hidden gtm-product-data"]/text()').extract()
        for json_string in my_json:
            parsed_json = json.loads(json_string)
            yield {'id': parsed_json['id'], 'name': parsed_json['name'].replace('\n', ' ').replace('\r', ''), 'position': parsed_json['position'], 'list': parsed_json['list'], 'price': parsed_json['price'], 'brand': parsed_json['brand']}