from django.conf.urls import url

from . import views
from .views import Q_host
from .views import Q_history

app_name = 'zabbix'

urlpatterns = [
    url(r'^$', views.index),
    url(r'^index/', views.index, name='zabbixindex'),
    url(r'^query/', Q_host.as_view(), name='Q_host'),
    url(r'^history/', Q_history.as_view(), name='Q_history'),
]
