import tensorflow as tf

class StockDataSet(object):
    def __init__(self,
                 stock_symbol,
                 features,
                 input_size=1,
                 num_steps=30,
                 test_ratio=0.1,
                 normalized=True,
                 close_price_only=True,
                ) -> tf.data.Dataset:
        self.stock_symbol = stock_symbol
        self.features = features,
        self.input_size = input_size
        self.num_steps = num_steps
        self.test_ratio = test_ratio
        self.close_price_only = close_price_only
        self.normalized = normalized
        pass

    def info(self):
        return "StockDataSet [%s] train: %d test: %d" % (
            self.stock_sym, len(self.train_X), len(self.test_y))

    def _prepare_data(self, seq):
        pass

    def generate_one_epoch(self, batch_size):
        pass
