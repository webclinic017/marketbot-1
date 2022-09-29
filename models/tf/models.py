from tabnanny import verbose
import tensorflow as tf
from tensorflow.keras.layers import LSTM, Dropout, Dense
from tensorflow.keras.losses import Huber 
from tensorflow.keras.optimizers import Adam
from tensorflow.keras import Sequential


class LongShortTermMemory(tf.keras.Model):
    def __init__(self, loss='rmse', opt='Adam', target='percentChangeOC'):
        self.target = target
        self.model = None
        super().__init__()

    @property
    def metrics(self):
        metrics = [ 
            tf.keras.metrics.MeanSquaredError(name='mse'), 
            tf.keras.metrics.MeanAbsoluteError(name='mae'),
            tf.keras.metrics.RootMeanSquaredError(name='rmse')
        ]
        return metrics
    
    @property
    def callbacks(self):
        callbacks = [
            # tf.keras.callbacks.EarlyStopping(monitor='loss', patience=5, mode='min', verbose=1), 
            tf.keras.callbacks.ModelCheckpoint(filepath='models/tf/checkpoints/model.{epoch:02d}-{loss:.4f}.h5', verbose=1),
        ]
        return callbacks

    def compile_model(self, X_train, prediction_range=100, optimizer='Adam', loss='huber', verbose=0) -> tf.keras.Model:
        model = Sequential()
        
        # 1st LSTM layer
        # * units = add prediction_range number of neurons (the dimensionality of the output space)
        # * return_sequences = True to stack LSTM layers so the next LSTM layer has a three-dimensional sequence input
        # * input_shape -> Shape of the training dataset
        model.add(LSTM(units=prediction_range, return_sequences=True, input_shape=(X_train.shape[1], 1)))

        # 1st Dropout layer: 20% of the layers will be dropped
        model.add(Dropout(0.2))
        
        # 2nd LSTM layer
        # * units = add prediction_range / 2 number of neurons (the dimensionality of the output space)
        # * return_sequences = True to stack LSTM layers so the next LSTM layer has a three-dimensional sequence input
        model.add(LSTM(units=prediction_range // 2, return_sequences=True))

        # 2nd Dropout layer: 20% of the layers will be dropped
        model.add(Dropout(0.2))

        # 3rd LSTM layer
        # * units = add prediction_range / 2 number of neurons (the dimensionality of the output space)
        # * return_sequences = True to stack LSTM layers so the next LSTM layer has a three-dimensional sequence input
        model.add(LSTM(units=prediction_range // 2, return_sequences=True))

        # 3rd Dropout layer: 50% of the layers will be dropped
        model.add(Dropout(0.5))

        # 4th LSTM layer
        # * units = add 50 neurons is the dimensionality of the output space
        model.add(LSTM(units=prediction_range // 2))

        # 50% of the layers will be dropped
        model.add(Dropout(0.5))

        # Dense layer that specifies an output of one unit
        model.add(Dense(units=1))

        if verbose > 0: model.summary()
        self.model = model
        self.model.compile(optimizer=optimizer, loss=loss, metrics=self.metrics)

    def train_model(self, X_train, y_train, epochs=25, verbose=0):
        if self.model is None:
            raise TypeError('Model has not been created yet! (received None type as input to trainer)')
        history = self.model.fit(X_train, y_train, epochs=epochs, verbose=verbose, callbacks=self.callbacks)

    def test_model(self, X_test, y_test, verbose=0):
        self.model.evaluate(X_test, y_test, verbose=verbose, callbacks=self.callbacks)

    def plot_train_metrics(self):
        # TODO:
        pass