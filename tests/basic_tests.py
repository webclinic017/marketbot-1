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
    @unittest.skip('in order to minimize API calls')
    def test_data_extraction_tda(self):
        if DEBUG: 
            print('TEST 1: Data Download and Feature Extraction')
            sleep(1.0)
        tda_client = client_connect('TDA', 'private/creds.ini')
        self.assertEqual(type(tda_client), Client)
        if DEBUG: print('[ TD Ameritrade API, Symbol: BLK ]')
        data = get_data(tda_client, symbol='BLK', period='TEN_YEAR', period_type='YEAR', frequency='DAILY', frequency_type='DAILY',
                        features= { 
                            'EMA': {}
                        }, api='TDA', save=False)
        if DEBUG: print(data)
    
    def test_dataset_model_compile_train(self):
        if DEBUG:
            print('\nTEST 2: Dataset Processing and Model Compiling/Training')
            sleep(1.0)
        data = StockDataGenerator('BLK', 'data/TDA/BLK/BLK_2012-09-06 05:00:00_2022-09-06 05:00:00.csv')
        lstm = LongShortTermMemory()
        lstm.create_model(data.X_train, verbose=DEBUG)
        lstm.train_model(data.X_train, data.y_train, verbose=DEBUG)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', default='False')
    args = parser.parse_args()
    sys.argv[1:] = args
    unittest.main()