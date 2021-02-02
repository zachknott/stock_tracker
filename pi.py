# for displaying prices on the sense hat

import time as t
import os
import requests
import bs4
from bs4 import BeautifulSoup
from requests_own import request_head
from requests_own import make_url
from sense_hat import SenseHat

import variables

sense = sense_hat()

NUM_STONKS_HAT = 1

def main():
    time_before = t.localtime().tm_sec

    requests_list = []
    price_list = []

    for x in range(NUM_STONKS_HAT):
        requests_list.append(requests.get(variables.URL_LIST[x]))

    for x in range(NUM_STONKS_HAT):
        price_list.append(request_head(requests_list[x]))  
    
    for x in range(NUM_STONKS_HAT):
        sense.show_message(variables.SYMBOL_LIST[x] + ": " + price_list[x])

    time_after = t.localtime().tm_sec

    refresh_time = variables.REFRESH_TIME_SECONDS - (time_after - time_before)

    if refresh_time < 0:
        refresh_time = 0

    t.sleep(refresh_time)


if __name__ == "__main__":
    # LOOP to run
    while(True):
        main()
    


