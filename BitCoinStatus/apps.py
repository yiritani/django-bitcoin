import json
from datetime import datetime

import requests
from django.apps import AppConfig


class BitcoinstatusConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'BitCoinStatus'




    # print(response['result'].items())

    # for i in response['result'].items():
    #     print(i)
