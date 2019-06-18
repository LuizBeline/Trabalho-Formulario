"""form URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import  include, url
from cadastro.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = ('cadastro.views',
url(r'^$', 'home', name='home'),
url(r'^cadastro/$', Criar.as_view(), name='cadastro'),
url(r'^lista/$', Lista.as_view(), name='lista'),
url(r'^admin/', include(admin.site.urls)),
)