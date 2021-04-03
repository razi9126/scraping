# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class OurfirstscraperPipeline:
    ## This function gets called each time we yield a value in our main code
    def process_item(self, item, spider):

        return item
