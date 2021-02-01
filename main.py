import bs4
import requests
from bs4 import BeautifulSoup
import time as t
import os

url_list = ['https://finance.yahoo.com/quote/GME',
            'https://finance.yahoo.com/quote/AMC',
            'https://finance.yahoo.com/quote/BB',
            'https://finance.yahoo.com/quote/NOK']

name_list = ['GME','AMC','BB','NOK']

NUM_STONKS = 4

def make_soup(name):
    soup = bs4.BeautifulSoup(name.text, features="html.parser")
    price = soup.find_all("div", {'class': 'D(ib) Mend(20px)'})[0].find('span').text
    return price

archive1 = 0
archive2 = 0

while(True):
    requests_list = []
    
    for url in url_list:
        requests_list.append(requests.get(url))
    
    price_list = []

    for request in requests_list:
        price_list.append(make_soup(request))

    os.system('cls' if os.name == 'nt' else 'clear')
    print("==============================")
    for x in range(NUM_STONKS):
        print(name_list[x] + " price: " + price_list[x])
    
    print("Time: " + t.asctime())
    print("==============================")

    t.sleep(1)
    


