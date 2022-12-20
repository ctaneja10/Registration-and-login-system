from django.contrib import admin
from django.urls import path
from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('creation/', views.creationpage, name='creation'),
    path('handlesignup/', views.handlesignup, name='signup'),
    path('handlelogin/', views.handleLogin, name='login'),
    path('handleLogout/', views.handleLogout, name='logout'),
]