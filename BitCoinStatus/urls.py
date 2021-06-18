from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path("price/", views.Index.as_view(), name="index"),
    path("price/applications/api/price", views.call_get_price_api, name="getPrice")
]
