from api.creds import client_connect
from api.tdameritrade.tech.overlap import BBANDS
import matplotlib.pyplot as plt
<<<<<<< refs/remotes/origin/main

tda_client = client_connect('TDA', 'private/creds.ini')
date, upper, middle, lower = BBANDS(tda_client, 'NVDA', tda_client.PriceHistory.PeriodType.MONTH, 
                                tda_client.PriceHistory.Period.SIX_MONTHS, tda_client.PriceHistory.FrequencyType.DAILY, 
                                tda_client.PriceHistory.Frequency.DAILY)
plt.plot(lower)
=======
import datetime

tda_client = client_connect('TDA', 'private/creds.ini')
date, close, upper, middle, lower = BBANDS(tda_client, 'NVDA', tda_client.PriceHistory.PeriodType.MONTH, 
                                tda_client.PriceHistory.Period.SIX_MONTHS, tda_client.PriceHistory.FrequencyType.DAILY, 
                                tda_client.PriceHistory.Frequency.DAILY)
plt.plot(date, lower, label='lower')
plt.plot(date, upper, label='upper')
plt.plot(date, middle, label='middle')
>>>>>>> Update README
plt.show()