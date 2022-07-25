import string
import talib as ta
from tda.client import Client
import numpy as np
<<<<<<< refs/remotes/origin/main
=======
import datetime
>>>>>>> Update README
import json 

def BBANDS(client : Client, stock : string, period_type : Client.PriceHistory.PeriodType, 
        period : Client.PriceHistory.Period, frequency_type : Client.PriceHistory.FrequencyType,
        frequency : Client.PriceHistory.Frequency) -> tuple:
    '''
        Returns Bollinger Bands for specified stock, period, and frequency.

        Args:
            client (Client) : the connected TD Ameritrade client
            stock (string) : the stock to calculate for
            period_type (PeriodType) : 
    '''
    price_history = client.get_price_history(stock, 
                        period_type=period_type,
                        period=period,
                        frequency_type=frequency_type,
                        frequency=frequency
            ).json()

    candles = price_history['candles']
    close = []
    date = []
    
    for day in candles:
        close.append(day['close'])
    for day in candles:
        date.append(day['datetime'])
    
    upper, middle, lower = ta.BBANDS(np.array(close), matype=ta.MA_Type.EMA)

<<<<<<< refs/remotes/origin/main
    return (date, upper, middle, lower)
=======
    return (date, close, upper, middle, lower)
>>>>>>> Update README
