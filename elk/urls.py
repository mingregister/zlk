from django.conf.urls import url

from . import views

app_name = 'elk'

urlpatterns = [
    url(r'^$', views.index),
    url(r'^index/', views.index, name='elkindex'),
]
