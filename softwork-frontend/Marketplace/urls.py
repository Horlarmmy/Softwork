"""Marketplace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.urls import include, re_path
from django.contrib import admin
from django.conf import settings

admin.site.site_header = settings.ADMIN_SITE_HEADER

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^', include('appMarketplace.urls')),
    re_path(r'^accounts/', include('accounts.urls')),
    re_path(r'^freelancer/', include('freelancer.urls')),
    re_path(r'^employee/', include('employee.urls')),
    re_path(r'^aroundtheweb/', include('scraper.urls')),
    re_path(r'^details/', include('details.urls')),
    re_path(r'^message/', include('message.urls')),
]
