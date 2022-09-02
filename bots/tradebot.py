import asyncio
from bots.strategies import Strategy

class TradeBot:
    def __init__(self, strategy, auto_update_model: bool):
        self.strategy = strategy
        self.auto_update_model = auto_update_model
    
    def activate():
        # TODO:
        pass

    def deactivate():
        # TODO:
        pass

    def pause_trading():
        # TODO:
        pass

    def toggle_model_auto_update(self):
        if self.auto_update_model is True:
            print('Toggling automated model training and updating OFF')
            self.auto_update_model = False
            # TODO:
        else:
            print('Toggling automated model training and updating ON')
            self.auto_update_model = True
            #TODO: