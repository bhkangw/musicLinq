from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add),
    url(r'^addfav/(?P<id>\d+)$', views.addfav),
    url(r'^removefav/(?P<id>\d+)$', views.removefav),
    # url(r'^(?P<id>\d+)$', views.edit),
    url(r'^logout$', views.logout),
]
