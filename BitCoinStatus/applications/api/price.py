import configparser
import os
import datetime
import time

import requests
import hashlib

# ToDo 固定パスから読み込める様にしたい
# path = os.path.dirname(os.path.abspath('djangoBitcoint'))
# path = os.path.join(path, 'config.ini')
config = configparser.ConfigParser()
config.read('config.ini')


def generate_kind_of_time(base_time):
    # dt = datetime.datetime.fromtimestamp(base_time) + datetime.timedelta(hours=9)
    dt = datetime.datetime.fromtimestamp(base_time)

    result = {
        'truncate_hour': dt.replace(hour=0, minute=0, second=0, microsecond=0).strftime('%Y-%m-%d %H:%M:%S'),
        'truncate_minute': dt.replace(minute=0, second=0, microsecond=0).strftime('%Y-%m-%d %H:%M:%S'),
        'truncate_second': dt.replace(second=0, microsecond=0).strftime('%Y-%m-%d %H:%M:%S')
    }

    return result


class BitCoinData(object):
    def __init__(self):
        self.secret_key = hashlib.sha256(config['default']['SECRET'].encode('utf-8')).hexdigest()

        self.headers = {
            'ACCESS-KEY': config['default']['KEY'],
            'ACCESS-SIGN': self.secret_key,
            'Content-Type': 'application/json'}

    def get_price(self, product_code='BTC_JPY'):
        response = requests.get('https://api.cryptowat.ch/markets/bitflyer/btcjpy/ohlc?periods=86400').json()[
            'result'].items()

        # print('PPPPPPPPPPPPPPPPPPPPPPPPPP', response)

        for i in response:
            return i[1]

        # return requests.get(
        #     config['default']['BASE_URL'] + '/v1/ticker?product_code=' + product_code,
        #     headers=self.headers
        # )


def main(product_name):
    bitCoin = BitCoinData()
    bitCoinData = bitCoin.get_price(product_name)

    for i in bitCoinData:
        time_set = generate_kind_of_time(i[0])

        result = {
            'product_code': 'BTC_JPY',
            'open_price': i[1],
            'high_price': i[2],
            'low_price': i[3],
            'close_price': i[4],
            'truncate_hour_time': time_set['truncate_hour'],
            'truncate_minute_time': time_set['truncate_minute'],
            'truncate_second_time': time_set['truncate_second'],

        }

        # print('resultresultresultresult', result)
        # return result
        yield result



if __name__ == '__main__':
    print(main('BTC_JPY'))
    # print(config.sections())
