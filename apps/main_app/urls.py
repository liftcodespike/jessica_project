
from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^home$', views.index),
    url(r'^show/(?P<id>\d+)$', views.show),
    url(r'^comment/add$', views.addComment),
]
