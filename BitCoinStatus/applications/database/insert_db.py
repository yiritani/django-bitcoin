from datetime import datetime

import requests

from ...models import BitCoinData


def insert_data(bit_coin_data):
    print('AAA', bit_coin_data)
    b = BitCoinData(
        product_code=bit_coin_data['product_code'],
        open_price=bit_coin_data['open_price'],
        high_price=bit_coin_data['high_price'],
        low_price=bit_coin_data['low_price'],
        close_price=bit_coin_data['close_price'],
        truncate_hour_time=bit_coin_data['truncate_hour_time'],
        truncate_minute_time=bit_coin_data['truncate_minute_time'],
        truncate_second_time=bit_coin_data['truncate_second_time'],
        unixtime=bit_coin_data['unixtime']
    )
    b.save()


if __name__ == '__main__':
    response = requests.get('https://api.cryptowat.ch/markets/bitflyer/btcjpy/ohlc?periods=86400').json()[
        'result'].items()
    # print(response)
    for i in response:
        for j in i[1]:
            print(datetime.fromtimestamp(j[0]))
            input_data = {
                'truncate_second': datetime.fromtimestamp(j[0]),
                'open_price': j[1],
                'high_price': j[2],
                'low_price': j[3],
                'close_price': j[4],
                'product_code': 'BTC_JPY'
            }

            insert_data(input_data)