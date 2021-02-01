import requests
import bs4
from bs4 import BeautifulSoup

# Makes a list of URLS from the Symbol Names
def make_url(NUM_STONKS,SYMBOL_LIST):
    list = []
    for x in range(NUM_STONKS):
        list.append('https://finance.yahoo.com/quote/' + SYMBOL_LIST[x])
    return list
    
#gets requests from Yahoo Finance
def get_request(name):
    soup = bs4.BeautifulSoup(name.text, features="html.parser")
    price = soup.find_all("div", {'class': 'D(ib) Mend(20px)'})[0].find('span').text
    return price

