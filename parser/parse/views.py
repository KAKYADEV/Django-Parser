from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, FormView
from .models import ReqSite, ParsedData
from .forms import ReqSiteForm
from .tasks import start_background_parse


class MainPageView(FormView):
    template_name = 'parse/main_page.html'
    form_class = ReqSiteForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['header'] = ['Добро пожаловать на YouParse', 'Создайте новый запрос на парсинг сайта']
        context['input_paragraph'] = ['Название сайта', 'URL сайта']
        context['button'] = 'Отправить'
        return context
    
    def form_valid(self, form):
        form.save(commit=False)
        form.save()
        site_id = form.instance.id
        return redirect('req_site_detail', pk=site_id)


# def index(request):
#     if request.method == 'POST':
#         form = ReqSiteForm(request.POST)
#         if form.is_valid():
#             form.save(commit=False)
#             form.save()
#             site_id = form.instance.id
#             return redirect('req_site_detail', pk=site_id)
#     else:
#         form = ReqSiteForm()
    
#     context = {
#         'title': 'Главная страница',
#         'header': ['Добро пожаловать на YouParse', 'Создайте новый запрос на парсинг сайта'],
#         'input_paragraph': ['Название сайта', 'URL сайта'],
#         'button': 'Отправить',
#         'form': form,
#     }
#     return render(request, 'parse/main_page.html', context)

class ReqSiteListView(ListView):

    model = ReqSite
    template_name = 'parse/req_sites_list.html'
    context_object_name = 'sites'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список запросов'
        context['header'] = 'Список запросов'
        context['empty_message'] = 'Список запросов пуст'
        return context

def req_site_detail(request, pk):
    site = ReqSite.objects.get(pk=pk)
    context = {
        'title': f'Парсинг {site.name}',
        'header': f'Запрос на парсинг сайта "{site.name}", URL: {site.url}',
        'site': site,
    }
    return render(request, 'parse/req_site_detail.html', context)

def start_parse(request, pk):
    site = ReqSite.objects.get(pk=pk)
    
    if request.method == 'POST':
        start_background_parse.delay(pk)

    context = {
        'title': f'Парсинг {site.name} в работе...',
        'header': f'Парсинг {site.name} в работе...',
        'site': site,
    }

    return render(request, 'parse/parse_processing.html', context)

class ParsedDataDetailView(DetailView):
    model = ParsedData
    template_name = 'parse/parsed_data_detail.html'
    context_object_name = 'parsed_data'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Результаты парсинга'
        context['header'] = f'Результаты парсинга для сайта "{self.object.site.name}"'
        context['time_start'] = self.object.site.time_request
        context['time_end'] = self.object.time_response
        context['duration_time'] = self.object.duration_time
        context['site_title'] = self.object.title
        context['site_description'] = self.object.description
        context['site_keywords'] = self.object.keywords
        return context
