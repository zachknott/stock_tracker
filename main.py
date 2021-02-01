import bs4
import requests
from bs4 import BeautifulSoup
import time as t
import os

url_list = ['https://finance.yahoo.com/quote/GME',
            'https://finance.yahoo.com/quote/AMC',
            'https://finance.yahoo.com/quote/BB',
            'https://finance.yahoo.com/quote/NOK']

name_list = ['GME','AMC','BB_','NOK']

# How many STONKS do you want to iterate through
NUM_STONKS = 2
REFRESH_TIME_SECONDS = 5

def make_soup(name):
    soup = bs4.BeautifulSoup(name.text, features="html.parser")
    price = soup.find_all("div", {'class': 'D(ib) Mend(20px)'})[0].find('span').text
    return price

while(True):
    time_before = t.localtime().tm_sec

    requests_list = []
    price_list = []

    for x in range(NUM_STONKS):
        requests_list.append(requests.get(url_list[x]))
        price_list.append(make_soup(requests_list[x]))

    os.system('cls' if os.name == 'nt' else 'clear')
    print("==============================")

    for x in range(NUM_STONKS):
        print(name_list[x] + " price: " + price_list[x])
    
    print("Time: " + t.asctime())
    print("==============================")

    time_after = t.localtime().tm_sec

    t.sleep(REFRESH_TIME_SECONDS -( time_after - time_before))
    


