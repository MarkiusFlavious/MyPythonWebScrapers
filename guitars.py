import pandas
import requests
from bs4 import BeautifulSoup

headers = {'User-agent' : 'Chrome/90.0.4430.212'}
url = 'https://www.oosthavens.co.za/product-category/guitars/electric-guitars/'
page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')
item_list = soup.find_all(class_='product-col')

guitars = [item.find(class_='woocommerce-loop-product__title').get_text().strip() for item in item_list]

# It took a bit of trial and error making the prices list.
# The price must be either the marked down value or 'No Price'
# For items where there are 2 prices returned, the 2nd price is the marked down prices
# First I must check if there is a price and return 'No Price' if there is none to prevent a traceback error
# To get all the correct prices I had to select the last value in the list that gets returned into item. ie [-1]
prices = list()
for item in item_list :
    if (item.find_all(class_='woocommerce-Price-amount amount')) :
        prices.append(item.find_all(class_='woocommerce-Price-amount amount')[-1].get_text().strip().replace(',',''))
    else :
        prices.append('No Price')

guitar_table = pandas.DataFrame(
    {
        'Guitar' : guitars,
        'Price' : prices,
    })

print(guitar_table)

guitar_table.to_csv('guitars.csv')
