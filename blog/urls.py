from django.urls import path
from . import views

from django.contrib.auth import  views as django_views
urlpatterns =[
    path('' , views.home , name ='home-path'),
path('register/' , views.register_view , name ='register-path'),
path('login/' , views.login_view , name ='login-path'),
path('logout/' , views.logout_view , name ='logout-path'),

#path('login/' , django_views.LoginView.as_view(template_name = 'blog/login.html'), name ='login' ),
#path('logout/' , django_views.LogoutView.as_view(template_name = 'blog/logout.html') , name ='logout-path'),
path('profile/' , views.profile, name = 'profile-path'),
path('edit_profile/' , views.edit_profile, name = 'edit_profile-path'),
]