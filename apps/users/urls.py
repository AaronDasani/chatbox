from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^create/$', views.create, name="create"),
    url(r'^(?P<id>\d+)/update/$', views.update, name="update"),
    url(r'^(?P<id>\d+)/destroy/$', views.destroy, name="destroy"),
    url(r'^new/$', views.new, name="new"),
    url(r'^(?P<id>\d+)/edit/$', views.edit, name="edit"),
    url(r'^(?P<id>\d+)/$', views.show, name="show"),
    url(r'^main/$', views.main, name="main"),
    url(r'^login/$', views.login, name="login"),
    url(r'^pokes/$', views.pokes, name="pokes"),
    url(r'^logout/$', views.logout, name="logout"),
]