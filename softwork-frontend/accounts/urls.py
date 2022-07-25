from django.urls import re_path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'accounts'

urlpatterns = [

    re_path(r'^login/$', views.login_view, name="login"),
#    url(r'^login/$', auth_views.login, {'template_name': 'accounts/login_form.html'}, name="login"),
#    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name="logout"),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), {'next_page': '/accounts/login/'}, name="logout"),
    re_path(r'^employeesignup/$', views.SignUpViewE, name="e_reg"),
    re_path(r'^freelancersignup/$', views.SignUpViewF, name="f_reg"),
#    url(r'^freelancersignup/$', views.UserFormView.as_view(), name="f_reg"),

]
