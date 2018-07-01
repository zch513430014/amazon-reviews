# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy



class CateItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    level = scrapy.Field()
    pid = scrapy.Field()
    pass

class AsinBestItem(scrapy.Item):
    asin = scrapy.Field()
    cid = scrapy.Field()
    rank = scrapy.Field()
    pass

class DetailItem(scrapy.Item):
    asin = scrapy.Field()
    image = scrapy.Field()
    title = scrapy.Field()
    star = scrapy.Field()
    used = scrapy.Field()
    reviews = scrapy.Field()
    seller_price = scrapy.Field()
    amazon_price = scrapy.Field()
    #
    used_price = scrapy.Field()
    saving_price = scrapy.Field()
    lighting_price = scrapy.Field()
    cid = scrapy.Field()
    rank = scrapy.Field()
    pass

class ReviewProfileItem(scrapy.Item):
    asin = scrapy.Field()
    product = scrapy.Field()
    brand = scrapy.Field()
    seller = scrapy.Field()
    image = scrapy.Field()
    review_total = scrapy.Field()
    review_rate = scrapy.Field()
    pct_five = scrapy.Field()
    pct_four = scrapy.Field()
    pct_three = scrapy.Field()
    pct_two = scrapy.Field()
    pct_one = scrapy.Field()
    pass


class ReviewDetailItem(scrapy.Item):
    asin = scrapy.Field()
    review_id = scrapy.Field()
    reviewer = scrapy.Field()
    review_url = scrapy.Field()
    star = scrapy.Field()
    date = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    pass


class KeywordRankingItem(scrapy.Item):
    skwd_id = scrapy.Field()
    rank = scrapy.Field()
    date = scrapy.Field()


class SalesRankingItem(scrapy.Item):
    rank = scrapy.Field()
    classify = scrapy.Field()
    asin = scrapy.Field()


class SDealsItem(scrapy.Item):
    thread_id = scrapy.Field()
    cur_price = scrapy.Field()
    his_price = scrapy.Field()
    relative_img = scrapy.Field()
    absolute_img = scrapy.Field()
    title = scrapy.Field()
    desc = scrapy.Field()
    amazon_url = scrapy.Field()
    origin_url = scrapy.Field()
    category = scrapy.Field()
    extra = scrapy.Field()
    hot = scrapy.Field()