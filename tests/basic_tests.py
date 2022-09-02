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
from models.tf.dataset import StockDataGenerator
from models.tf.models import LongShortTermMemory
import unittest

''' Test Data Download and Feature Extraction '''
class TestBasics(unittest.TestCase):

    def test_data_extraction_tda(self):
        print('TEST 1: Data Download and Feature Extraction')
        tda_client = client_connect('TDA', 'private/creds.ini')
        self.assertEqual(type(tda_client), Client)
        print('[ TD Ameritrade API, Symbol: BLK ]')
        data = get_data(tda_client, symbol='BLK', period='TEN_YEAR', period_type='YEAR', frequency='DAILY', frequency_type='DAILY',
                        features= { 
    
                        }, api='TDA', save=True)
        print(data)
    
    def test_model_compile_train(self):
        dataset = StockDataGenerator('NDAQ', 'data/TDA/NDAQ/NDAQ_2012-08-27_2022-08-26.csv')
        X_train, y_train, X_test, y_test = dataset.split_data()
        lstm = LongShortTermMemory()
        lstm.create_model(X_train)
        lstm.train_model(X_train, y_train)


if __name__ == '__main__':
    unittest.main()