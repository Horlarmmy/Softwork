from django.urls import re_path
from . import views

app_name = 'scraper'

urlpatterns = [
    re_path(r'^$', views.ScraperView, name = "aroundtheweb"),
]
