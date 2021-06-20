import json
from datetime import datetime

import requests
from django.db.models import Q
from django.http import HttpResponse
from django.views.generic import ListView
from . import models
from .applications.api import price
from .applications.database import insert_db, select_db


class Index(ListView):
    model = models.BitCoinData

    def get_queryset(self):
        q_word = self.request.GET.get('query')

        if q_word:
            object_list = models.BitCoinData.objects.filter(
                Q(title__icontains=q_word) | Q(author__icontains=q_word))
        else:
            object_list = models.BitCoinData.objects.all()
        return object_list


def call_get_price_api(request):
    product = ''
    # print(request.GET)
    if 'product_code' in request.GET:
        product = request.GET['product_code']

    response = price.main(product)
    # print('AAAAAAA',response)
    insert_db.insert_data(response)
    select_db.select_data()


    return HttpResponse(response)
