from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('all', all),
    path('animation', animation),
    path('print', print),
    path('brand', brand),
    path('mobile', mobile)
]
