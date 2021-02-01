import time as t
import os
import requests
import bs4
from bs4 import BeautifulSoup
from requests_own import get_request
from requests_own import make_url




if __name__ == "__main__":

    # Add Symbols to the stock tracker
    SYMBOL_LIST = ['GME','AMC','BB','NOK','VTI',"VOO"]
    # How many symbols do you want to iterate through
    NUM_STONKS = 2
    # what refresh time in seconds
    REFRESH_TIME_SECONDS = 5

    # Warning
    STOCK_NUM = 0
    PRICE = 245
    

    # Setup runs once
    url_list2 = make_url(NUM_STONKS,SYMBOL_LIST)

    # LOOP to run
    while(True):
        time_before = t.localtime().tm_sec

        requests_list = []
        price_list = []

        for x in range(NUM_STONKS):
            requests_list.append(requests.get(url_list2[x]))
            price_list.append(get_request(requests_list[x]))

        os.system('cls' if os.name == 'nt' else 'clear')            # Clears the terminal
        print("==============================")

        for x in range(NUM_STONKS):
            print(SYMBOL_LIST[x] + " price: " + price_list[x])

            if float(price_list[STOCK_NUM]) > PRICE:
                print("\a")
    
        print("Time: " + t.asctime())
        print("==============================")

        time_after = t.localtime().tm_sec

        refresh_time = REFRESH_TIME_SECONDS - (time_after - time_before)

        if refresh_time < 0:
            refresh_time = 0

        t.sleep(refresh_time)
    


