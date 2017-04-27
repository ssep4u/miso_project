from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^wordCloud/$', views.wordCloud, name='wordCloud'),
    url(r'^wordForm/$', views.wordForm, name='wordForm'),
]
