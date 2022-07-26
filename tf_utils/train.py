import tensorflow as tf
import getopt
from model import create_lstm_model
import sys

def main(argv):
    opts, args = getopt.getopt(argv, 'hm:d:e')

    model = create_lstm_model(X_train)

    history = model.fit(
        X_train, y_train,
        epochs=50,
        batch_size=32,
        shuffle=False
    )