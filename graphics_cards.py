import pandas
import requests
from bs4 import BeautifulSoup

url = 'https://www.evetech.co.za/components/nvidia-ati-graphics-cards-21.aspx'
page = requests.get(url)
page_soup = BeautifulSoup(page.content, 'html.parser')

card_soup = page_soup.find_all(class_="fst")

card_names = [item.find(class_="myProductName").get_text().strip() for item in card_soup]
card_prices = [item.find(class_="price").get_text().replace('Including VAT','').replace(',','').strip() for item in card_soup]
card_extra_info = [item.find(class_="ExtraInfoBtn").get_text().strip() for item in card_soup]

card_stock = list()
for item in card_soup :
    if item.find(class_="statuslbl_Out") : card_stock.append('Out of Stock')
    if item.find(class_="statuslbl_In") : card_stock.append('In Stock with Evetech')

graphics_card_table = pandas.DataFrame(
    {
        'Graphics Card' : card_names,
        'Price' : card_prices,
        'Stock' : card_stock,
        'Extra Information' : card_extra_info,
    })

print(graphics_card_table)

graphics_card_table.to_csv('Evetech_Graphics_Cards.csv')
print('===============================================================================\n')
print('===============================| Saved to CSV |================================')
