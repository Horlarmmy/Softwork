from django.urls import re_path
from . import views

app_name = 'message'

urlpatterns = [

    re_path(r'^list/(?P<user_id>[0-9]+)/$', views.message, name='message'),

]
