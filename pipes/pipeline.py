from sklearn.pipeline import Pipeline
from scikeras.wrappers import KerasRegressor
from models.tf.models import LongShortTermMemory
from data.dataset import StockDataGenerator
from sklearn.model_selection import KFold, GridSearchCV
from joblib import Memory

feature_combos = [ 
    { 
        'EMA': {},
        '%B': {},
        'CCI': {}, 
        'RSI': {}, 
        'VIX': {}
    }, 
    {
    }
]
for i, features in enumerate(feature_combos):
    print(f'Feature Set {i + 1}/' + str(len(feature_combos)))
    data = StockDataGenerator(
            'BLK', api='TDA',
            period='FIVE_YEAR', period_type='YEAR', 
            frequency='DAILY', frequency_type='DAILY',
            features=features, verbose=1, target='close', 
            lookback=0, pc=True 
    )
    model = LongShortTermMemory()
    lstm = KerasRegressor(model=model.compile_model(data.X_train, verbose=0))
    model_pipeline = Pipeline([
        ('lstm', lstm)
    ])
    model_params = {
        'lstm__epochs': 25, 'lstm__verbose': 1,
    }
    model_pipeline.fit(data.X_train, data.y_train, **model_params)