from utils.get_data import download_data, extract_features
from api.creds import client_connect
from tda.client import Client
import json

tda_client = client_connect('TDA', 'private/creds.ini')
data = download_data(tda_client, symbol='NVDA', period='ONE_YEAR', period_type='YEAR', frequency='DAILY', frequency_type='DAILY')
_ = json.loads(data) # test for valid json
df = extract_features(['BBANDS', 'DEMA', 'EMA', 'HT_TRENDLINE', 'KAMA', 'MA'], data)
# print('SUCCESS')