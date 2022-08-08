import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import LSTM, Dropout, Dense
from tensorflow.keras import Sequential

class LongShortTermMemory:
    def get_metrics(self):
        metrics = [ tf.keras.metrics.MeanSquaredError(name='MSE') ]
        return metrics

    def get_callbacks():
        callbacks = [
            tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=3, mode='min', verbose=1), 
            tf.keras.callbacks.ModelCheckpoint(filepath='model.{epoch:02d}-{val_loss:.2f}.h5')
        ]
        return callbacks

    def create_model(self, X_train, prediction_range=100) -> keras.Model:
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
        model.add(LSTM(units=prediction_range / 2, return_sequences=True))

        # 2nd Dropout layer: 20% of the layers will be dropped
        model.add(Dropout(0.2))

        # 3rd LSTM layer
        # * units = add prediction_range / 2 number of neurons (the dimensionality of the output space)
        # * return_sequences = True to stack LSTM layers so the next LSTM layer has a three-dimensional sequence input
        model.add(LSTM(units=prediction_range / 2, return_sequences=True))

        # 3rd Dropout layer: 50% of the layers will be dropped
        model.add(Dropout(0.5))

        # 4th LSTM layer
        # * units = add 50 neurons is the dimensionality of the output space
        model.add(LSTM(units=prediction_range / 2))

        # 50% of the layers will be dropped
        model.add(Dropout(0.5))

        # Dense layer that specifies an output of one unit
        model.add(Dense(units=1))

        model.summary()
        return model