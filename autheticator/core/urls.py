from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.signupPage, name='signup'),
    path('login/', views.loginPage, name='login'),
    path('home/', views.homePage, name='home'),
]
