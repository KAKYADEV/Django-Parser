from django.contrib import admin as dj_admin
from django.urls import path, include
 
urlpatterns = [
    path('admin/', dj_admin.site.urls),
    path('parse/', include('parse.urls')),
]
