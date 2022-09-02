from utils.data import get_data
from api.creds import client_connect
from tda.client import Client
import json
from tda import client
import pandas as pd
from talib import get_functions
import numpy as np
import logging
from typing import Union
import unittest

''' Test Data Download and Feature Extraction '''
class TestBasics(unittest.TestCase):

    def test_data_extraction_tda(self):
        print('TEST 1: Data Download and Feature Extraction')
        tda_client = client_connect('TDA', 'private/creds.ini')
        self.assertEqual(type(tda_client), Client)
        print('[ TD Ameritrade API, Symbol: NDAQ ]')
        data = get_data(tda_client, symbol='NDAQ', period='TWO_YEAR', period_type='YEAR', frequency='DAILY', frequency_type='DAILY',
                        features= { 
                                    'EMA': {'timeperiod': 5}, 'CCI': {'timeperiod': 5}, 
                                    'ROC': {'timeperiod': 4}, 'RSI': {'timeperiod': 4}, 'WILLR': {'timeperiod': 5},
                                    'MACD': {'fastperiod': 12, 'slowperiod': 26, 'signalperiod': 9}
                        }, api='TDA', save=True)
        print(data)

if __name__ == '__main__':
    unittest.main()