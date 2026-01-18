from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db import models
from .models import ReqSite
  
def index(request):
    context = {
        'title': 'Главная страница',
        'header': 'Добро пожаловать на YouParse'
    }
    return render(request, 'parse/main_page.html', context)

def req_site_list(request):
    site_list = ReqSite.objects.all()
    context = {
        'title' : 'Список запросов',
        'header' : 'Список запросов',
        'site_list': site_list,
    }
    return render(request, 'parse/req_sites_list.html', context)
