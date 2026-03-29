from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, FormView
from .models import ReqSite, ParsedData
from .forms import ReqSiteForm
from .tasks import start_background_parse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404


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
        user = self.request.user
        form.instance.user = user
        form.save(commit=False)
        form.save()
        site_id = form.instance.id
        return redirect('req_site_detail', pk=site_id)

class ReqSiteListView(ListView):

    model = ReqSite
    template_name = 'parse/req_sites_list.html'
    context_object_name = 'sites'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Request Sites List'
        context['header'] = 'Request Sites List'
        context['empty_message'] = 'Request Sites List is empty'
        return context

def req_site_detail(request, pk):
    sites = ReqSite.objects.filter(user=request.user)
    site = get_object_or_404(sites, pk=pk)
    context = {
        'title': f'Parsing {site.name}',
        'header': f'Request for parsing website "{site.name}", URL: {site.url}',
        'site': site,
    }
    return render(request, 'parse/req_site_detail.html', context)

def start_parse(request, pk):
    sites = ReqSite.objects.filter(user=request.user)
    site = get_object_or_404(sites, pk=pk)
    
    if request.method == 'POST':
        start_background_parse.delay(pk)

    context = {
        'title': f'Parsing {site.name} is running...',
        'header': f'Parsing {site.name} is running...',
        'site': site,
    }

    return render(request, 'parse/parse_processing.html', context)

class ParsedDataDetailView(DetailView):
    model = ParsedData
    template_name = 'parse/parsed_data_detail.html'
    context_object_name = 'parsed_data'

    def get_queryset(self):
        return super().get_queryset().filter(site__user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Parsed Data for {self.object.site.name}'
        context['header'] = f'Parsed Data for Website "{self.object.site.name}"'
        context['time_start'] = self.object.site.time_request
        context['time_end'] = self.object.time_response
        context['duration_time'] = self.object.duration_time
        context['site_title'] = self.object.title
        context['site_description'] = self.object.description
        context['site_keywords'] = self.object.keywords
        context['site_headers'] = self.object.headers
        context['site_images'] = self.object.images_preview
        context['seo_score'] = self.object.seo_score
        return context

class RegisterUserView(CreateView):
    template_name = 'parse/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Register New User'
        context['header'] = 'Registration of New User'
        context['button'] = 'Register'
        return context

class LoginUserView(LoginView):
    template_name = 'parse/login.html'
    authentication_form = AuthenticationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Log in'
        context['header'] = 'Log in to System'
        context['button'] = 'Log in'
        return context

def logout_user(request):
    logout(request)
    return redirect('index')