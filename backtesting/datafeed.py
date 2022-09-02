import backtrader as bt
import pandas as pd
from talib import get_functions as technical_indicators

class DataFeed(bt.feed.DataBase):
    def __init__(self, dataset: pd.DataFrame):
        super().__init__()
        self.dataset = dataset
        self.params = (
            ('datetime', None), 
            ('open', -1), 
            ('close', -1), 
            ('high', -1),
            ('low', -1),
            ('volume', -1)
            (indicator, -1 if indicator in 
                self.dataset.columns.values else None) 
                for indicator in technical_indicators()
        )