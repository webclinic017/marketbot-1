from tda.client.synchronous import Client as TDA_Client
from coinbase.wallet.client import Client as CB_Client
import pandas as pd
from pandas import DataFrame
import json
import talib as ta
import inspect

def download_data(client : TDA_Client, log=False, **kwargs):
    if isinstance(client, TDA_Client):
        stock = kwargs['stock']
        period = kwargs['period']
        period_type = kwargs['period_type']
        frequency = kwargs['frequency']
        frequency_type = kwargs['frequency_type']

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

        price_history = client.get_price_history(stock, 
                            period_type=all_period_types[period_type], 
                            period=all_periods[period], 
                            frequency=all_frequencies[frequency]
                        )

        return price_history.json()

def extract_features(features : list, json_string : str) -> DataFrame:
    data = json.loads(json_string)
    for func in features:
        if func in ta.get_functions():
            feature = getattr(ta, func)
            params = inspect.getargspec(feature)
            # TODO: extract all necessary values for the possible 
            #       parameters for features
            #   possible params:
            #	    required: close, periods, high, low, open, volume
            #	    optional: timeperiod, minperiod, maxperiod, matype, 
            #                 acceleration, maximumu, fastperiod, 
            #                 slowperiod, signal period, fastmatype, 
            #                 slowmatype, signalmatype, fastk_period, 
            #                 slowk_period, slowk_matype, slowd_period, 
            #                 slowd_matype, timeperiod1, timeperiod2, 
            #                 timeperiod3, penetration
    return None

