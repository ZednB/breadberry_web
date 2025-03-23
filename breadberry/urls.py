from django.urls import path

from breadberry.apps import BreadberryConfig
from breadberry.views import *

app_name = BreadberryConfig.name

urlpatterns = [
    path('', home, name='base'),
    path('breakfast_list/', breakfast_list, name='breakfast')
]