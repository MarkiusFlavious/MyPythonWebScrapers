# Some Simple Web Scrapers

Just a few basic web scrapers I made. They all use Pandas to create a csv file containing the scraped data.  

## 1. watches.py  
>While playing around on [Bid or Buy](https://www.bidorbuy.co.za), I learned that for their site, I needed to use a json payload in order to get the results I wanted in Beautiful Soup, which was to grab the 1st page's search results for watches.

## 2. graphics_cards.py  
>[Evetech](https://www.evetech.co.za) have a webpage for their Nvidia cards. This pulls the card name and price as well as additional information. Right now it's mostly just saying "free shipping," but at the time that I wrote this script, the crypto market was at its all time high and the additional info field was mostly saying "out of stock."

## 3. guitars.py  
>This one was fun to make. A [small South African music shop](https://www.oosthavens.co.za) with some... interesting HTML. I learned how to deal with handling 2 prices for a guitar or no price.

## 4. cologne.py  
>[Takealot](https://www.takealot.com) was rejecting my scraper when using the requests module, so I used Selenium to scrape the information instead.
