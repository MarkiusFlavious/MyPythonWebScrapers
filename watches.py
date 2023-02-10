import pandas
import requests
from bs4 import BeautifulSoup

payload = {
    'mode' : 'execute',
    'submitter' : 'HeaderSearchForm',
    'isInteractive' : 'true',
    'sellerSearchUrl' : 'https://www.bidorbuy.co.za/jsp/usersearch/UserNameSearch.jsp?UserNameChars=',
    'IncludedKeywords' : 'fitness watches',
    'CategoryId' : '622'
    }

url = 'https://www.bidorbuy.co.za/jsp/tradesearch/TradeSearch.jsp'

page = requests.post(url, data=payload)
page.encoding = 'gzip'
soup = BeautifulSoup(page.text, 'lxml')

blocks = soup.find_all(class_="tradelist-grid-item-link")

watch_names = [name.find(class_="tradelist-item-title").get_text().strip() for name in blocks]
prices = [price.find(class_="font-weight-bold").get_text().strip() for price in blocks]
offer_ends = [offer.find(class_="d-none d-md-block text-darker font-sm mt-2").get_text().strip() for offer in blocks]

watch_table = pandas.DataFrame(
    {
        'Watche' : watch_names,
        'Price' : prices,
        'Info' : offer_ends,
    })

print(watch_table)

watch_table.to_csv('watches.csv')
