from api.creds import client_connect

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

# TODO:
try:
    raise(ConnectionError)
    print('Kraken:          UP')
except:
    print('Kraken:         DOWN')