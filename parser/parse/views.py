from django.http import HttpResponse
from django.shortcuts import render, redirect
  
def index(request):
    context = {
        'title': 'Главная страница',
        'header': 'Добро пожаловать на YouParse'
    }
    return render(request, 'parse/main_page.html', context)
