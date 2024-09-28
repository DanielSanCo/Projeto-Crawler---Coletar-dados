import scrapy
class NomeDaClasseSpider(scrapy.Spider):
    name = 'coletardados'
    def start_requests(self):
        urls = ['https://www.goodreads.com/quotes']
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
    def parse(self,response):
        for elemento in response.xpath("//div[@class='quoteDetails']"):
            yield {
                'citacao': elemento.xpath(".//div[@class='quoteText']/text()").get(),
                'autor': elemento.xpath(".//span[@class='authorOrTitle']/text()").get(),
                'tags': elemento.xpath(".//div[@class='greyText smallText left']/a/text()").getall()
            }