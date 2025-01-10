from django.urls import  path

from portfolio import settings
from project import views
from django.conf.urls.static import static


# this is the url pattern for the project app
urlpatterns = [
    path('', views.home_page, name='home'),  
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
]

# this is for photos to be displayed in the browser
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)