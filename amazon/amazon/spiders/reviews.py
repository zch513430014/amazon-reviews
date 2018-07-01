# -*- coding: utf-8 -*-
import scrapy
from amazon.helper import Helper
class ReviewsSpider(scrapy.Spider):
    name = 'reviews'
    allowed_domains = ['amazon.com']
    # custom_settings = {
    #     'LOG_LEVEL': 'ERROR',
    #     'LOG_FILE': 'review_detail.json',
    #     'LOG_ENABLED': True,
    #     'LOG_STDOUT': True
    # }
    def __init__(self,asin=None, *args, **kwargs):
        self.asin = asin
        self.start_urls = [
            'https://www.amazon.com/product-reviews/%s?sortBy=recent&filterByStar=three_star' % self.asin,
            'https://www.amazon.com/product-reviews/%s?sortBy=recent&filterByStar=two_star' % self.asin,
            'https://www.amazon.com/product-reviews/%s?sortBy=recent&filterByStar=one_star' % self.asin
        ]
        pass

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.get_detail)


    def parse(self, response):
        reviews = response.css('.review-views .review')
        for row in reviews:
            print(row.css('.review-title::text')[0].extract())

    def get_detail(self, response):
        # 获取评价总数
        total = response.css('.AverageCustomerReviews .totalReviewCount::text').extract()  # 获取评价总数
        now_total = Helper.get_num_split_comma(total[0])
        print(now_total)
