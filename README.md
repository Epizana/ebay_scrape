# ebay_scrape
Scraping snapshot of sales from ebay's action figure cateogry. The purpose of the project is to take a brief look at the sales volume for different brands/IPs (if possible, based on user-provided data).

The crawler aims to scrape sold listings form eBay's action figure category for details including selling price, title, brand, franchise/IP, number of bids, quantity sold, and a few other categorical features. Because eBay sold listings follow 3 general "formats" (auction, buy-it-now/BIN, and "dutch" style auctions, where a given quantity is offered for sale and the actual listing page is only qualified as completed/sold when the whole batch is sold out; until that occurs the page remains "live") coupled with the item specifics data being largely user/seller populated, many values for the categorical features may or may not be present.

Except for title and price, all other categories will populate based on a combination of user input and/or auction format.

For example, BIN formats will have 0 for number of bids, while "dutch" style auctions will most likely not list a sell date, as the actual listing itself remains live even though some of the offered quantity has sold. The brand/'character family' value-which will be used for the sales volume analysis for a given brand-is unfortunately user provided information and may or may not be populated.

v1.0
At this time, there is no functionality yet to consider text from seller-provided descriptions, as well as capturing dutch-style auction listings.
