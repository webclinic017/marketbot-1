from dataclasses import dataclass
import tensorflow as tf
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from utils.data import download_data, extract_features

class StockDataSet(object):
    def __init__(self,
                 symbol : str,
                 data_path : str,
                 input_size=1,
                 num_steps=30,
                 test_ratio=0.15,
                 normalized=True,
                 close_price_only=True
                 ) -> tf.data.Dataset:
        self.symbol = symbol
        self.input_size = input_size
        self.num_steps = num_steps
        self.test_ratio = test_ratio
        self.close_price_only = close_price_only
        self.normalized = normalized
        self.data = pd.read_csv(data_path)

    def info(self):
        return "StockDataSet [%s] train: %d test: %d" % (
            self.symbol, len(self.train_X), len(self.test_y)
        )

    def _prepare_data(self, seq):
        if self.normalized:
            self.data = np.log(self.data) - np.log(self.data.shift(1))

    def generate_one_epoch(self, batch_size):
        pass
