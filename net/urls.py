from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.net_list, name='index'),
    url(r'^list$', views.net_list, name='net_list'),
    url(r'^add$', views.net_add, name='net_add'),
    url(r'^edit/(?P<pk>\d+)$', views.net_edit, name='net_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.net_delete, name='net_delete'),
]
