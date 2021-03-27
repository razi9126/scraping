import scrapy


class RedditbotSpider(scrapy.Spider):
    name = 'redditbot'

    start_urls = ['https://www.reddit.com/r/MaliciousCompliance/']

    def parse(self, response):
        # print(response.text)
        titles = response.xpath('//*[@class="_eYtD2XCVieq6emjKBH3m"]/text()').extract()
        votes = response.css('._1rZYMD_4xY3gRcSS3p8ODO::text').extract()
        comments = response.css('.FHCV02u6Cp2zYL0fhQPsO::text').extract()
        
        print(titles)
        print(votes)
        print(comments)
        for (title, vote, comment) in zip(titles, votes, comments):        
            yield {'Title': title.encode('utf-8'), 'Vote': vote, "Comments": comment}