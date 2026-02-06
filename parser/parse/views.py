from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import ReqSite
from .forms import ReqSiteForm
from .tasks import start_background_parse

  
def index(request):
    if request.method == 'POST':
        form = ReqSiteForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            site_id = form.instance.id
            return redirect('req_site_detail', pk=site_id)
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

def req_site_detail(request, pk):
    site = ReqSite.objects.get(pk=pk)
    context = {
        'title': f'Парсинг {site.name}',
        'header': f'Запрос на парсинг сайта "{site.name}", URL: {site.url}',
        'site': site,
    }
    return render(request, 'parse/req_site_detail.html', context)

def start_parse(request, pk):
    if request.method == 'POST':
        site = ReqSite.objects.get(pk=pk)
        site.status = ReqSite.Site.PROCESSING
        site.save(update_fields=['status'])

        start_background_parse.delay(pk)

    else:
        site = ReqSite.objects.get(pk=pk)

    context = {
        'title': f'Парсинг {site.name} в работе...',
        'header': f'Парсинг {site.name} в работе...',
        'site': site,
    }

    return render(request, 'parse/parse_processing.html', context)
