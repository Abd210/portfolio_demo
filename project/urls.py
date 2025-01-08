from django.contrib import admin
from django.urls import include, path

from portfolio import settings
from project import views
from django.conf.urls.static import static


urlpatterns = [
    path('', views.projects_list), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)