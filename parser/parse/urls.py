from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('sites/', req_site_list, name='req_site_list'),
    path('sites/<int:pk>/', req_site_detail, name='req_site_detail'),
    path('sites/<int:pk>/start_parse/', start_parse, name='start_parse'),
]