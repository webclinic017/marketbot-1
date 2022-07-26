from datetime import datetime
from tda.client.synchronous import Client as TDA_Client
from coinbase.wallet.client import Client as CB_Client
import pandas as pd
from pandas import DataFrame
import json
import talib as ta
import numpy as np
from typing import Union
from tqdm import tqdm

def download_data(client : Union[TDA_Client, CB_Client], log=False, **kwargs):
    if isinstance(client, TDA_Client):
        all_frequencies = {
            'ONE_MIN': client.PriceHistory.Frequency.EVERY_MINUTE,
            'FIVE_MIN': client.PriceHistory.Frequency.EVERY_FIVE_MINUTES,
            'TEN_MIN': client.PriceHistory.Frequency.EVERY_TEN_MINUTES,
            'FIFTEEN_MIN': client.PriceHistory.Frequency.EVERY_FIFTEEN_MINUTES,
            'THIRTY_MIN': client.PriceHistory.Frequency.EVERY_THIRTY_MINUTES,
            'DAILY': client.PriceHistory.Frequency.DAILY,
            'WEEKLY': client.PriceHistory.Frequency.WEEKLY,
            'MONTHLY': client.PriceHistory.Frequency.MONTHLY
        }
        all_frequency_types = {
            'MINUTE': client.PriceHistory.FrequencyType.MINUTE,
            'DAILY': client.PriceHistory.FrequencyType.DAILY,
            'WEEKLY': client.PriceHistory.FrequencyType.WEEKLY,
            'MONTHLY': client.PriceHistory.FrequencyType.MONTHLY
        }
        all_periods = {
            'ONE_YEAR': client.PriceHistory.Period.ONE_YEAR,
            'TWO_YEARS': client.PriceHistory.Period.TWO_YEARS,
            'THREE_YEARS': client.PriceHistory.Period.THREE_YEARS,
            'FIVE_YEARS': client.PriceHistory.Period.FIVE_YEARS,
            'TEN_YEARS': client.PriceHistory.Period.TEN_YEARS,
            'FIFTEEN_YEARS': client.PriceHistory.Period.FIFTEEN_YEARS,
            'YEAR_TO_DATE': client.PriceHistory.Period.YEAR_TO_DATE,
            'ONE_MONTH': client.PriceHistory.Period.ONE_MONTH,
            'TWO_MONTHS': client.PriceHistory.Period.TWO_MONTHS,
            'THREE_MONTHS': client.PriceHistory.Period.THREE_MONTHS,
            'SIX_MONTHS': client.PriceHistory.Period.SIX_MONTHS,
            'ONE_DAY': client.PriceHistory.Period.ONE_DAY,
            'TWO_DAYS': client.PriceHistory.Period.TWO_DAYS,
            'THREE_DAYS': client.PriceHistory.Period.THREE_DAYS,
            'FOUR_DAYS': client.PriceHistory.Period.FOUR_DAYS,
            'FIVE_DAYS': client.PriceHistory.Period.FIVE_DAYS
        }
        all_period_types = {
            'DAY': client.PriceHistory.PeriodType.DAY,
            'MONTH': client.PriceHistory.PeriodType.MONTH,
            'YEAR': client.PriceHistory.PeriodType.YEAR,
            'YEAR_TO_DATE': client.PriceHistory.PeriodType.YEAR_TO_DATE
        }
        params = {
            'symbol': kwargs['symbol'], 
            'period_type': all_period_types[kwargs['period_type']], 
            'period': all_periods[kwargs['period']], 
            'frequency_type': all_frequency_types[kwargs['frequency_type']], 
            'frequency': all_frequencies[kwargs['frequency']],
            'need_extended_hours_data': 'true'
        }
        payload = { key: val for key, val in params.items() if val!=None}

        data = json.dumps(client.get_price_history(**payload).json(), indent=4)
        return data
    # TODO: Coinbase API Compatibility
    # elif isinstance(client, CB_Client):
    # TODO: Kraken API Compatibility


def extract_features(features : list, json_string : str) -> DataFrame:
    data = json.loads(json_string)
    vars = {
        'open': np.array([ candle['open'] for candle in data['candles'] ]),
        'close': np.array([ candle['close'] for candle in data['candles'] ]),
        'high': np.array([ candle['high'] for candle in data['candles'] ]),
        'low': np.array([ candle['low'] for candle in data['candles'] ]),
        'volume': np.array([ candle['volume'] for candle in data['candles'] ]),
        'datetime': np.array([ pd.to_datetime(candle['datetime'], unit='ms') for candle in data['candles'] ])
    }

    for func in tqdm(features):
        if func in ta.get_functions():
            if func == 'BBANDS':
                upperband, middleband, lowerband = getattr(ta, 'BBANDS')(vars['close'], matype=ta.MA_Type.EMA)
                vars['UPPER_BBAND'] = upperband
                vars['MIDDLE_BBAND'] = middleband
                vars['LOWER_BBAND'] = lowerband
            elif func == 'DEMA':
                vars['DEMA'] = getattr(ta, 'DEMA')(vars['close'])
            elif func == 'EMA':
                vars['EMA'] = getattr(ta, 'EMA')(vars['close'])
            elif func == 'HT_TRENDLINE':
                vars['HT_TRENDLINE'] = getattr(ta, 'HT_TRENDLINE')(vars['close'])
            elif func == 'KAMA':
                vars['KAMA'] = getattr(ta, 'KAMA')(vars['close'])
            elif func == 'MA':
                vars['MA'] = getattr(ta, 'MA')(vars['close'], matype=ta.MA_Type.EMA)
            else: pass
    df = DataFrame.from_dict(vars)
    df.index = df['datetime']
    return df
    ################################################################
    # TODO: extract all necessary values for the possible          #
    #       parameters for features                                #
    #   possible params:                                           #
    #	    required: close, periods, high, low, open, volume      #
    #	    optional: timeperiod, minperiod, maxperiod, matype,    #
    #                 acceleration, maximumu, fastperiod,          #
    #                 slowperiod, signal period, fastmatype,       #
    #                 slowmatype, signalmatype, fastk_period,      #
    #                 slowk_period, slowk_matype, slowd_period,    #
    #                 slowd_matype, timeperiod1, timeperiod2,      #
    #                 timeperiod3, penetration                     #
    ################################################################