import time as t
import os
import requests
import bs4
from bs4 import BeautifulSoup


#Add Symbols to the stock tracker
SYMBOL_LIST = ['GME','AMC','BB','NOK','VTI',"VOO"]
# How many symbols do you want to iterate through
NUM_STONKS = 6
# what refresh time in seconds
REFRESH_TIME_SECONDS = 10

#gets requests from Yahoo Finance
def get_request(name):
    soup = bs4.BeautifulSoup(name.text, features="html.parser")
    price = soup.find_all("div", {'class': 'D(ib) Mend(20px)'})[0].find('span').text
    return price

# Makes a list of URLS from the Symbol Names
def make_url(NUM_STONKS):
    list = []
    for x in range(NUM_STONKS):
        list.append('https://finance.yahoo.com/quote/' + SYMBOL_LIST[x])
    return list

# Setup runs once
url_list2 = make_url(NUM_STONKS)

# LOOP to run
while(True):
    time_before = t.localtime().tm_sec

    requests_list = []
    price_list = []

    for x in range(NUM_STONKS):
        requests_list.append(requests.get(url_list2[x]))
        price_list.append(get_request(requests_list[x]))

    os.system('cls' if os.name == 'nt' else 'clear')        # Clears the terminal
    print("==============================")

    for x in range(NUM_STONKS):
        print(SYMBOL_LIST[x] + " price: " + price_list[x])
    
    print("Time: " + t.asctime())
    print("==============================")

    time_after = t.localtime().tm_sec

    refresh_time = REFRESH_TIME_SECONDS - (time_after - time_before)

    if refresh_time < 0:
        refresh_time = 0

    t.sleep(refresh_time)
    


