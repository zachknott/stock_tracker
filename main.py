import bs4
import requests
from bs4 import BeautifulSoup
import time as t
import os

def make_soup(name):
    soup = bs4.BeautifulSoup(name.text, features="html.parser")
    price = soup.find_all("div", {'class': 'D(ib) Mend(20px)'})[0].find('span').text
    return price

archive1 = 0
archive2 = 0

while(True):
    
    url_1 = requests.get('https://finance.yahoo.com/quote/GME')
    url_2 = requests.get('https://finance.yahoo.com/quote/AMC')
    url_3 = requests.get('https://finance.yahoo.com/quote/BB')

    gme = (make_soup(url_1))
    amc = (make_soup(url_2))
    bb =  (make_soup(url_3))

    print1 = "GME price: " + gme
    print2 = "AMC price: " + amc
    print3 = "BB price: " + bb
    
    
    os.system('cls' if os.name == 'nt' else 'clear')

    print("==============================")
    print(print1)
    print(print2)
    print(print3)
    print("Time: " + t.asctime())
    print("==============================")

    t.sleep(1)
    


