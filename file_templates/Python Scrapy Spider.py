import scrapy
from bs4 import BeautifulSoup

#set($class_name = ${StringUtils.firstLetterCaps(${NAME})})
#set($spider_name = $class_name.toLowerCase())

class ${class_name}Spider(scrapy.Spider):
    name = "${spider_name}"
    base_url = "<url>"

    def start_requests(self):
        queries = []
        urls = [self.base_url + q for q in queries]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        goods = []
        for info in BeautifulSoup(response.body, 'html.parser').findAll(attrs={"class": "<class>"}):
            pass
            
        [print(x) for x in goods]
