from sklearn.pipeline import Pipeline
from scikeras.wrappers import KerasRegressor
from models.tf.models import LongShortTermMemory
from data.dataset import StockDataGenerator
from sklearn.model_selection import KFold, GridSearchCV
from joblib import Memory
from sklearn.base import BaseEstimator
from xgboost import XGBRegressor, XGBRFRegressor
from sklearn.metrics import make_scorer, mean_squared_error
from sklearn.model_selection import TimeSeriesSplit
from pipes.steps import ClfSwitcher


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
            period='TEN_YEAR', period_type='YEAR',
            frequency='DAILY', frequency_type='DAILY',
            features=features, verbose=1, target='close', 
            lookback=0, pc=True 
    )

    lstm = LongShortTermMemory()
    lstm.compile_model(data.X_train, verbose=1, name=f'lstm_{i + 1}')
    lstm_nn = KerasRegressor(model=lstm.model)
    boosted_trees = XGBRegressor()
    boosted_forests = XGBRFRegressor()
    
    model_pipeline = Pipeline([
        ('clf', ClfSwitcher()),
    ])

    model_params = [
    
        {
            'clf__estimator': [boosted_trees],
            'clf__estimator__learning_rate': [0.0001, 0.001, 0.01, 0.1, 1.0, 2.0, 3.0]
        },

        {
            'clf__estimator': [boosted_forests],
        },

        {
            'clf__estimator': [lstm_nn],
            'clf__estimator__epochs': [50],
            'clf__estimator__verbose': [1]
        }
        
    ]

    splitter = TimeSeriesSplit(n_splits=3, gap=0, test_size=len(data.y_test))
    splits = splitter.split(data.X)
    cv = GridSearchCV(
        model_pipeline, model_params, cv=splits, 
        n_jobs=1, verbose=1, scoring=make_scorer(
            mean_squared_error, greater_is_better=False
        )
    )
    cv.fit(data.X, data.y)