from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.netmap_list, name='index'),
    url(r'^list$', views.netmap_list, name='netmap_list'),
    url(r'^add$', views.netmap_add, name='netmap_add'),
    url(r'^edit/(?P<pk>\d+)$', views.netmap_edit, name='netmap_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.netmap_delete, name='netmap_delete'),
]
