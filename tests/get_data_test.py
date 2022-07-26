from utils.get_data import download_data, extract_features
from api.creds import client_connect
from tda.client import Client
import json
from talib import get_functions
import time

tda_client = client_connect('TDA', 'private/creds.ini')
# data = download_data(tda_client, symbol='NVDA', period='ONE_YEAR', period_type='YEAR', frequency='DAILY', frequency_type='DAILY')
print('Starting download...')
dl_start = time.time()
data = download_data(tda_client, symbol='NVDA', period='ONE_YEAR', period_type='YEAR', frequency='DAILY', frequency_type='DAILY')
print(f'Download complete! ({time.time() - dl_start} seconds)')
_ = json.loads(data) # test for valid json
print('Extracting features...')
ext_start = time.time()
df = extract_features([ 'BBANDS', 'DEMA', 'EMA', 'HT_TRENDLINE', 'KAMA', 'MA' ], data)
# df = extract_features([ _ for _ in get_functions() ], data)
print(f'Features extracted! ({time.time() - ext_start} seconds)')
print('SUCCESS')
print(df)