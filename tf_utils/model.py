import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import LSTM, Dropout, Dense

def create_lstm_model(X_train, prediction_range=250) -> keras.Model:
    model = keras.Sequential()
    model.add(keras.layers.LSTM(prediction_range, input_shape=(X_train.shape[1], X_train.shape[2])))
    model.add(keras.layers.Dropout(0.2))
    model.add(keras.layers.Dense(1))
    model.compile(loss='mae', optimizer='adam')
    model.summary()
    return model