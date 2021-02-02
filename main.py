import time as t
import os
import requests
import bs4
from bs4 import BeautifulSoup
from requests_own import request_head
from requests_own import make_url

import variables


def main():
    time_before = t.localtime().tm_sec

    requests_list = []
    price_list = []

    for x in range(variables.NUM_STONKS):
        requests_list.append(requests.get(variables.URL_LIST[x]))

    for x in range(variables.NUM_STONKS):
        price_list.append(request_head(requests_list[x]))
        
    os.system('cls' if os.name == 'nt' else 'clear')            # Clears the terminal
    print("==============================")
    
    for x in range(variables.NUM_STONKS):
        print(variables.SYMBOL_LIST[x] + " price: " + price_list[x])

        if x == variables.STOCK_NUM and (float(price_list[variables.STOCK_NUM]) > variables.MAX_PRICE or float(price_list[variables.STOCK_NUM]) < variables.MIN_PRICE):
            print("\a")

    print("Time: " + t.asctime())

    if t.localtime().tm_hour >= 20 or t.localtime().tm_hour < 4:
        print("\nTRADING CLOSED FOR THE DAY\n")
    print("==============================")

    time_after = t.localtime().tm_sec

    refresh_time = variables.REFRESH_TIME_SECONDS - (time_after - time_before)

    if refresh_time < 0:
        refresh_time = 0

    t.sleep(refresh_time)


if __name__ == "__main__":
    # LOOP to run
    while(True):
        main()
    


