from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import ReqSite
from .forms import ReqSiteForm
  
def index(request):
    if request.method == 'POST':
        form = ReqSiteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/parse/sites/')
    else:
        form = ReqSiteForm()
    
    context = {
        'title': 'Главная страница',
        'header': ['Добро пожаловать на YouParse', 'Создайте новый запрос на парсинг сайта'],
        'input_paragraph': ['Название сайта', 'URL сайта'],
        'button': 'Отправить',
        'form': form,
    }
    return render(request, 'parse/main_page.html', context)

def req_site_list(request):
    site_list = ReqSite.objects.all()
    context = {
        'title' : 'Список запросов',
        'header' : 'Список запросов',
        'empty_message' : 'Список запросов пуст',
        'site_list': site_list,
    }   
    return render(request, 'parse/req_sites_list.html', context)
