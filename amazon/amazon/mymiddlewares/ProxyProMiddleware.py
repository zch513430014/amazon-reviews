import json
import random
class ProxyProMiddleware(object):
    def __init__(self):
        with open('proxy.json', 'r') as f:
            self.proxies = json.load(f)
    def process_request(self, request, spider):
        request.meta['proxy'] = 'http://{}'.format(random.choice(self.proxies))
