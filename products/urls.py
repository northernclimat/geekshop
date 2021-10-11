from django.urls import path
from .views import index, products

app_name = 'products'

urlpatterns = [
    path('', products, name='ind'),
    path('index/', index, name='index'),
    path('', products, name='products'),
]