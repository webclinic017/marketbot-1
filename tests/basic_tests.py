from utils.data import get_data
from api.creds import client_connect
from tda.client import Client
from models.tf.dataset import StockDataGenerator
from models.tf.models import LongShortTermMemory
from time import sleep
import unittest
import sys
import argparse

class TestBasics(unittest.TestCase):
    ''' Tests for data downloading, feature creation, and basic training pipelines '''
    # @unittest.skip('in order to minimize API calls')
    def test_data_extraction_tda(self):
        tda_client = client_connect('TDA', 'private/creds.ini')
        self.assertEqual(type(tda_client), Client)
        print('\n[ TD Ameritrade API, Symbol: BLK ]')
        data = get_data(tda_client, symbol='BLK', period='TEN_YEAR', period_type='YEAR', frequency='DAILY', frequency_type='DAILY',
                        features= { 
                            'EMA': {}
                        }, api='TDA', save=False)
        if True: print(data)
    
    def test_dataset_model_compile_train(self):
        print('\n')
        data = StockDataGenerator('BLK', 'data/TDA/BLK/BLK_2012-09-06 05:00:00_2022-09-06 05:00:00.csv')
        lstm = LongShortTermMemory()
        lstm.create_model(data.X_train, verbose=2)
        lstm.train_model(data.X_train, data.y_train, verbose=2)

if __name__ == '__main__':
    unittest.main(verbosity=2)