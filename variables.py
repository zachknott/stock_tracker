from requests_own import make_url

#All MODIFIABLE VARIABLES#

# Add Symbols to the stock tracker
SYMBOL_LIST = ['GME','AMC','BB','NOK','VTI',"VOO"]
# How many symbols do you want to iterate through
NUM_STONKS = 2
# Makes URL List
URL_LIST = make_url(NUM_STONKS,SYMBOL_LIST)
# what refresh time in seconds
REFRESH_TIME_SECONDS = 10

# Warning Beep
STOCK_NUM = 0
MAX_PRICE = 300
MIN_PRICE = 50