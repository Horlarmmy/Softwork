from django.urls import re_path
from . import views

app_name = 'employee'

urlpatterns = [

    re_path(r'^$', views.e_home, name='e_home'),
    re_path(r'^add-job/$', views.add_job, name='add_job'),
#    url(r'^edit-job/$', views.edit_job, name='edit_job'),
    re_path(r'^profile/(?P<user_id>[0-9]+)/$', views.profile, name='profile'),
    re_path(r'^profile/edit-profile/(?P<user_id>[0-9]+)/$', views.edit_profile, name='edit_profile'),

]
