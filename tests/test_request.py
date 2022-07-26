from tda import client
from api.creds import client_connect
import json

c = client_connect('TDA', 'private/creds.ini')
r = c.get_price_history('AAPL',
        period_type=client.Client.PriceHistory.PeriodType.YEAR,
        period=client.Client.PriceHistory.Period.ONE_YEAR,
        frequency=client.Client.PriceHistory.Frequency.DAILY
    )
assert r.status_code == 200, r.raise_for_status()
# print(json.dumps(r.json(), indent=4))
print('SUCCESS')