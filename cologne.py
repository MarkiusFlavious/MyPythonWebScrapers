import pandas as p
from bs4 import BeautifulSoup as bs
from selenium import webdriver

print('Retrieving data... This takes about a minute...')

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
browser = webdriver.Chrome(options=options, executable_path=r'C:\Users\User\Documents\webdrivers\chromedriver.exe')
browser.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})

browser.get('https://www.takealot.com/all?_sb=1&_r=1&_si=08e77064246e3e6ac2bfcc9f79f2d49e&qsearch=cologne')
page_source = browser.page_source
soup = bs(page_source, 'html.parser')

blocks = (soup.find_all(class_="search-product grid"))

cologne_names = [name.find(class_="shiitake-children").get_text().strip() for name in blocks]
prices = [price.find_all(class_="currency plus currency-module_currency_29IIm")[0].get_text().strip() for price in blocks]
stock_infos = [stock.find(class_="cell shrink stock-availability-status").get_text().strip() for stock in blocks]

cologne_table = p.DataFrame(
    {
        'Cologne' : cologne_names,
        'Prices' : prices,
        'Stock' : stock_infos,
    })

print(cologne_table)

cologne_table.to_csv('cologne.csv')

browser.quit()
