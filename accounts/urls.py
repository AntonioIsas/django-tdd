from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from accounts import views

urlpatterns = [
    path('send_login_email', views.send_login_email, name='send_login_email'),
    path('login', views.login, name='login'),
    path('logout', LogoutView.as_view(next_page='/'), name='logout'),
]
