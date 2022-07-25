from django.urls import re_path
from . import views

app_name = 'freelancer'

urlpatterns = [

    re_path(r'^$', views.f_home, name='f_home'),
    re_path(r'^profile/(?P<user_id>[0-9]+)/$', views.profile, name='profile'),
    re_path(r'^profile/edit-profile/(?P<user_id>[0-9]+)/$', views.edit_profile, name='edit_profile'),


]
