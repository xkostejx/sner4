from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^net/', include('net.urls')),
    url(r'^job/', include('job.urls')),
]

