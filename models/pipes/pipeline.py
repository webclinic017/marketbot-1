from sklearn.pipeline import Pipeline
from scikeras.wrappers import KerasRegressor
from models.tf.models import LongShortTermMemory
from models.tf.dataset import StockDataGenerator
from sklearn.model_selection import KFold, GridSearchCV
from joblib import Memory
from api.data import get_data
data = StockDataGenerator(
            'BLK', 
            data_path='data/TDA/example.csv',
            verbose=1, target='close'
        )
model = LongShortTermMemory()
lstm = KerasRegressor(model=model.compile_model(data.X_train, verbose=0), verbose=0)
pipe1 = Pipeline([
    ('lstm', lstm)
])
params1 = {
    'lstm__epochs': 25, 'lstm__verbose': 1
}
pipe1.fit(data.X_train, data.y_train, **params1)