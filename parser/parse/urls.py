from django.urls import path
from .views import *


urlpatterns = [
    path('', MainPageView.as_view(), name='index'),
    path('sites/', ReqSiteListView.as_view(), name='req_site_list'),
    path('sites/<int:pk>/', req_site_detail, name='req_site_detail'),
    path('sites/<int:pk>/start_parse/', start_parse, name='start_parse'),
    path('sites/<int:pk>/results/', ParsedDataDetailView.as_view(), name='parsed_data_detail'),
]