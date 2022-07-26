from api.creds import client_connect
import krakenex
from pykrakenapi import KrakenAPI

print('      API      STATUS')

# connect to TDA API
try:
    tda_client = client_connect('TDA', 'private/creds.ini')
    print('TD Ameritrade:   UP')
except:
    print('TD Ameritrade:  DOWN')

# connect to Coinbase API
try:
    cb_client = client_connect('CB', 'private/creds.ini')
    print('Coinbase:        UP')
except:
    print('Coinbase:       DOWN')

try:
    api = krakenex.API()
    k = KrakenAPI(api)
    ohlc, last = k.get_ohlc_data("BCHUSD")
    print('Kraken:          UP')
except:
    print('Kraken:         DOWN')