import tensorflow as tf
import pandas as pd
from utils.data import download_data, extract_features

class StockDataSet(object):
    def __init__(self,
                 symbols : list,
                 data_path : str,
                 input_size=1,
                 num_steps=30,
                 test_ratio=0.1,
                 normalized=True,
                 close_price_only=True,
                ) -> tf.data.Dataset:
        self.input_size = input_size
        self.num_steps = num_steps
        self.test_ratio = test_ratio
        self.close_price_only = close_price_only
        self.normalized = normalized
        data = pd.read_csv(data_path)
        self.features = [ feat for feat in data.columns() ]
        pass

    def info(self):
        return "StockDataSet [%s] train: %d test: %d" % (
            self.stock_sym, len(self.train_X), len(self.test_y))

    def _prepare_data(self, seq):
        pass

    def generate_one_epoch(self, batch_size):
        pass
