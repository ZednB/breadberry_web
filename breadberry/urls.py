from django.urls import path

from breadberry.apps import BreadberryConfig
from breadberry.views import *

app_name = BreadberryConfig.name

urlpatterns = [
    path('', home, name='base'),
    path('breakfast_list/', breakfast_list, name='breakfast'),
    path('drink_list/', drink_list, name='drink'),
    path('salad_list/', salad_list, name='salad_list'),
    path('hot_list/', hot_list, name='hot_list'),
    path('saj_list/', saj_list, name='saj_list'),
    path('steak_list/', steak_list, name='steak_list'),
    path('paste_list/', paste_list, name='paste_list'),
    path('fastfood_list/', fastfood_list, name='fastfood_list'),
]