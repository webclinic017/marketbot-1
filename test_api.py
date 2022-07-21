import sys
import os
import importlib
import json
from 
# connect to TDA API
tda_client = client_connect('TDA', './private/creds.ini')
tda_quote = tda_client.get_quote('NVDA').json()
print(json.dumps(tda_quote, indent=4))

# connect to Coinbase API
cb_client = client_connect('CB', './private/creds.ini')
cb_quote = cb_client.get_buy_price(currency_pair='ETH-USD')
print(json.dumps(cb_quote, indent=4))