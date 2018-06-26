from django.conf.urls import url
from django.urls import path
 
from . import views
 
urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('<str:section>/', views.get_section, name='get_section'),
]

