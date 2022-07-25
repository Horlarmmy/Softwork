import re
from django.urls import re_path
from . import views

app_name = 'appMarketplace'

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^about/$', views.about, name='about'),
    re_path(r'^contact/$', views.contact_us, name='contact_us'),
]
