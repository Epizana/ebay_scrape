from scrapy import Spider, Request
from ebay.items import EbayItem
import re


class EbaySpider (Spider):
    name = 'ebay_spider' #this must always be a unqiue name!!!!!!
    allowed_domains = ['www.ebay.com']
    start_urls = ['https://www.ebay.com/sch/i.html?_dcat=246&_fsrp=1&_nkw=toys&_sacat=246&_from=R40&LH_Complete=1&rt=nc&LH_Sold=1&Type=Action%2520Figure']


    def parse(self, response):
        
        #get the total number of pages from the hit summary on the left-hand side.
        #hit_string = response.xpath('//h1[@class="srp-controls__count-heading"]/span/text()').extract_first()
        #total_hits = int(''.join(re.findall('\d+(?:\.\d+)?',hit_string)))
        #per_page = 50 #ebay seems to default responses to 50 per page. 
        #number_pages = total_hits // per_page

        
        #store long url, and construct all the urls for the resulting pages.
        temp = 'https://www.ebay.com/sch/i.html?_dcat=246&_fsrp=1&_nkw=toys&_sacat=246&_from=R40&LH_Complete=1&rt=nc&LH_Sold=1&Type=Action%2520Figure&_pgn={}'

        page_urls = [temp.format(x) for x in range(1,260)] #try 250

        
        for url in page_urls: #yield 2 for now
            yield Request(url=url, callback = self.parse_result_page)

    def parse_result_page(self, response):


        item_urls = response.xpath('//a[@class="s-item__link"]/@href').extract()
        #print(len(item_urls)) #print how many urls gathered per page. Apparently default is 50?
        #print('='*50)

        for url in item_urls:
            yield Request(url, callback=self.parse_item_page)

    def parse_item_page(self, response):

        title = response.xpath('//span[@id="vi-lkhdr-itmTitl"]/text()').extract_first()
        
        item_num = int(response.xpath('//div[@class="u-flL iti-act-num itm-num-txt"]/text()').extract_first())

        try:
            condition = response.xpath('//div[@itemprop="itemCondition"]/text()').extract_first()
        except:
            condition = 'None'


        #BIN page has different xpath from auction page. Try BIN, exception is auction.

        try:
            price1 = response.xpath('//span[@class="notranslate"]/text()').extract_first().lstrip()
        except:
            price1 = response.xpath('//span[@class="notranslate vi-VR-cvipPrice" or @id="mm-saleDscPrc"]/text()').extract_first()
        
        #process either BIN or auction price with below:
        price = float(''.join(re.findall('\d+(?:\.\d+)?',price1)))
        
        #not all results will be auction format. 0 bids is BIN/dutch auction.

        try:
            bids = int(response.xpath('//a[@class="vi-bidC"]/span/text()').extract_first())
        except:
            bids = 0

        #dutch-style auctions show quantity sold. If not dutch style, quant_sold = 1.

        try:
            quant_sold = response.xpath('//a[@class="vi-txt-underline"]/text()').extract_first()
            quant_sold = quant_sold = int(''.join(re.findall('\d+',quant_sold)))
        except:
            quant_sold = 1

        try:
            category = response.xpath('//td[@style="vertical-align:top;"]/table/tr/td/ul/li[5]//text()').extract_first()
        except:
            category = ''


        #store pages with multiple quantities will not have a sold date on the results page
        #as long as there is item stock.
        try:
            sell_date = response.xpath('//span[@id="bb_tlft"]/text()').extract_first().lstrip()
        except:
            sell_date = ''

        #++++++++++++++process Item specifics box++++++++++++++++
        
        #overall xpath for the table
        temp = response.xpath('//div[@class="itemAttr"]')
        #xpath for the categories and their text values, yields messy list.
        item_specifics = temp.xpath('.//table//tr//td//text()').extract()
        #process the messy list
        specs = list(filter(lambda s: s != '',list(map(lambda s: s.strip(),item_specifics))))
        
        #dict comprehension for key/value assignment; list --> dict
        item_dict = {specs[i][:-1]:specs[i+1] for i in range (0,len(specs)-1) if ':' in specs[i]}

        #user-provided individual specifics may or may not be populated on a given page.
        
        try:
            brand = response.xpath('//h2[@itemprop="brand"]/span/text()').extract_first()
        except:
            brand = ''

        try:
            year = item_dict['Year']
        except:
            year = ''

        try:
            era = item_dict['Era']
        except:
            era = ''

        try:
            franchise = item_dict['Character Family']
        except:
            franchise = ''
        
        try:
            character = item_dict['Character']
        except:
            character = ''

        try:
            toy_type = item_dict['Type']
        except:
            toy_type = ''

        try:
            size = item_dict['Size']
        except:
            size = ''

        #+++++++++++++assign items++++++++++++++++
        
        item = EbayItem()
        item['title'] = title
        item['item_num'] = item_num
        item['condition'] = condition
        item['price'] = price
        item['bids'] = bids
        item['quantity_sold'] = quant_sold
        item['category'] = category
        item['brand'] = brand
        item['year'] = year
        item['era'] = era
        item['franchise'] = franchise
        item['character'] = character
        item['toy_type'] = toy_type
        item['sell_date'] = sell_date
        item['size'] = size
        yield item



        #print('+'*20,'Processed', title,'+'*20)
