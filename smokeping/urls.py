from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^targets/$', views.targets),
    url(r'^alerts/$', views.alerts),
    url(r'^parents/$', views.parents),
    url(r'^slaves/$', views.slaves),
    url(r'^probes/$', views.probes),
    url(r'^export/$', views.export),
    url(r'^secrets/$', views.secrets),
]
