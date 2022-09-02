from dataclasses import dataclass
from locale import normalize
import tensorflow as tf
import pandas as pd
import numpy as np
from datetime import datetime as dt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import scale

class StockDataGenerator(object):
    def __init__(self, symbol : str, data_path : str, target='close',
                 num_steps=30, test_ratio=0.15, normalized=True,
                 close_price_only=True) -> tf.data.Dataset:
        self.symbol = symbol
        self.num_steps = num_steps
        self.test_ratio = test_ratio
        self.close_price_only = close_price_only
        self.normalized = normalized
        self.data = pd.read_csv(data_path, index_col='datetime')
        self.num_features = len(self.data.columns) - 1 
        self.target = target

    def info(self):
        return "StockDataSet [%s] train: %d test: %d" % (
            self.symbol, len(self.train_X), len(self.test_y)
        )

    def get_num_features(self): return self.num_features

    def _prepare_data(self, lookback=2):
        self.data['percentChange'] = self.data['close'] / self.data['open'] - 1
        # self.data.index = [ dt.strptime(date, '%Y-%m-%d %I:%M:%S') for date in self.data.index.values]
        for i in range(1, lookback + 1):
            self.data[f'percentChange-{i}'] = self.data['percentChange'].shift(-lookback)
        self.data = pd.DataFrame(scale(X=self.data), index=self.data.index, columns=self.data.columns)
    
    def split_data(self, test_percent=0.25):
        self._prepare_data()
        X = self.data.loc[:, self.data.columns != self.target]
        y = self.data.loc[:, self.data.columns == self.target]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_percent, random_state=42)
        X_train = X_train.to_numpy()
        y_train = y_train.to_numpy()
        X_test = X_test.to_numpy()
        y_test = y_test.to_numpy()
        return X_train, y_train, X_test, y_test
    
    def generate_windows(self):
        pass

        # if self.normalized:
        #     self.data['%B'] = (self.data['close'] - self.data['LOWER_BBAND']) / (self.data['UPPER_BBAND'] - self.data['LOWER_BBAND'])
