import requests
import time as t
import bs4
from bs4 import BeautifulSoup

# Makes a list of URLS from the Symbol Names
def make_url(NUM_STONKS,SYMBOL_LIST):
    list = []
    for x in range(NUM_STONKS):
        list.append('https://finance.yahoo.com/quote/' + SYMBOL_LIST[x])
    return list


def request_head(name):
    if t.localtime().tm_hour >= 16 or (t.localtime().tm_hour <= 9 and t.localtime().tm_min <= 30):
        return get_request_extended(name)
    else:
        return get_request_active(name)

#gets requests from Yahoo Finance
def get_request_active(name):
    soup = bs4.BeautifulSoup(name.text, features="html.parser")
    price = soup.find_all("div", {'class': 'D(ib) Mend(20px)'})[0].find('span').text
    return price

def get_request_extended(name):
    soup = bs4.BeautifulSoup(name.text, features="html.parser")
    price = soup.find_all("p", {'class': 'Fz(12px) C($tertiaryColor) My(0px) D(ib) Va(b)'})[0].find('span').text
    return price
