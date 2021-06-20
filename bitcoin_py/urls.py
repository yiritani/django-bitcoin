from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.views.generic import TemplateView

index_view = TemplateView.as_view(template_name='registration/index.html')
price_view = TemplateView.as_view(template_name='BitCoinStatus/bitcoindata_list.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("pass/", login_required(index_view), name="index"),
    path('', include("django.contrib.auth.urls")),
    path('', include("BitCoinStatus.urls")),
    path('price/', login_required(price_view), name="price"),
]
