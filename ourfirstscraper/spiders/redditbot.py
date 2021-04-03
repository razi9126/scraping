import scrapy
from ..items import OurfirstscraperItem

class RedditbotSpider(scrapy.Spider):
    
    name = 'redditbot'

    start_urls = ['https://www.reddit.com/r/MaliciousCompliance/']

    def parse(self, response):

        ## Import the item class for data storage from items.py
        item = OurfirstscraperItem()

        # print(response.text)
        titles = response.xpath('//*[@class="_eYtD2XCVieq6emjKBH3m"]/text()').extract()
        votes = response.css('._1rZYMD_4xY3gRcSS3p8ODO::text').extract()
        comments = response.css('.FHCV02u6Cp2zYL0fhQPsO::text').extract()
        
        # print(titles)
        # print(votes)
        # print(comments)
        for (title, vote, comment) in zip(titles, votes, comments):        
            # Storing the extracted data into the items class we created
            item['titles'] = title
            item['comments'] = comment
            item['votes'] = vote

            # yield {'Title': title.encode('utf-8'), 'Vote': vote, "Comments": comment}
            yield item
