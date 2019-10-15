# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.exceptions import DropItem
from scrapy.exporters import CsvItemExporter


#class ValidateItemPipeline(object): #change class name to validate item
    
    #def process_item(self, item, spider):
        #if not all(item.values()): #this function all sticks a true inbetween all the values. Basically returning if all values are true. So if NOT true, raise drop item.
         #   raise DropItem("Missing values!")
        #else:
         #   return item

class WriteItemPipeline(object): #can copy and paste into my own script! However changes the filename.

    def __init__(self):
        self.filename = 'ebay11.csv'

    def open_spider(self, spider):
        self.csvfile = open(self.filename, 'wb') #,/n = '' for windows.
        self.exporter = CsvItemExporter(self.csvfile)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.csvfile.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
