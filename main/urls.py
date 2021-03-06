"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^friends/', include('apps.friends.urls', namespace="friends")),
    url(r'^dashboard/', include('apps.Dashboard.urls', namespace="dashboard")),
    url(r'^likes/', include('apps.likes.urls', namespace="likes")),
    url(r'^pokes/', include('apps.pokes.urls', namespace="pokes")),
    url(r'^wall/', include('apps.message.urls', namespace="message")),
    url(r'^gaming/', include('apps.gaming.urls', namespace="games")),
    url(r'^', include('apps.users.urls', namespace="users"))
]
