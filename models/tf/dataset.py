import tensorflow as tf
import pandas as pd
import numpy as np
from datetime import datetime as dt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import scale
import matplotlib.pyplot as plt

class StockDataGenerator(object):
    def __init__(self, symbol : str, data_path : str, target='close',
                 num_steps=30, test_ratio=0.15, normalized=True,
                 close_price_only=True, verbose=0) -> tf.data.Dataset:
        self.symbol = symbol
        self.num_steps = num_steps
        self.test_ratio = test_ratio
        self.close_price_only = close_price_only
        self.normalized = normalized
        self.data = pd.read_csv(data_path, index_col='datetime')
        self.num_features = len(self.data.columns) - 1 
        self.target = target
        self._process_dataset()
        self.verbose = verbose

    def info(self):
        return "StockDataSet [%s] train: %d test: %d" % (
            self.symbol, len(self.train_X), len(self.test_y)
        )

    def get_num_features(self): return self.num_features

    def _process_dataset(self, lookback=2, normalization=True, test_percent=0.25, verbose=0):
        if verbose >= 1: print('Normalizing data...')
        self.data['percentChange'] = self.data['close'] / self.data['open'] - 1
        if verbose >= 1: print('Generating lookback features...')        
        for i in range(1, lookback + 1):
            self.data[f'percentChange-{i}'] = self.data['percentChange'].shift(-lookback)
        if verbose >= 1: print('Scaling data...')
        self.data = pd.DataFrame(scale(X=self.data), index=self.data.index, columns=self.data.columns)
        X = self.data.loc[:, self.data.columns != self.target]
        y = self.data.loc[:, self.data.columns == self.target]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_percent, random_state=42)
        self.X_train = X_train.to_numpy()
        self.y_train = y_train.to_numpy()
        self.X_test = X_test.to_numpy()
        self.y_test = y_test.to_numpy()
        return X_train, y_train, X_test, y_test
    
    def generate_window():
        # TODO:
        pass

    def plot_features(features: list):
        # TODO:
        pass