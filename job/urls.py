from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.job_list, name='index'),
    url(r'^list$', views.job_list, name='job_list'),
    url(r'^getwork$', views.job_getwork, name='job_getwork'),
    url(r'^show/(?P<pk>\d+)$', views.job_show, name='job_show'),
    url(r'^add$', views.job_add, name='job_add'),
    url(r'^delete/(?P<pk>\d+)$', views.job_delete, name='job_delete'),
]
