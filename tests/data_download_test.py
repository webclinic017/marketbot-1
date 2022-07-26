from utils.get_data import download_data, extract_features
from api.creds import client_connect
from tda.client import Client
import json

tda_client = client_connect('TDA', 'private/creds.ini')
ph = download_data(tda_client, stock='NVDA', period='ONE_YEAR', period_type='YEAR', frequency='DAILY', frequency_type='DAILY')
print(json.dumps(ph, indent=4))