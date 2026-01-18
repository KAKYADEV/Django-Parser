from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    path('sites/', req_site_list),
]