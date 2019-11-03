"""Определяет схемы URL для пользователей"""

from django.conf.urls import url
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

app_name = 'users'

urlpatterns = [
    # Страница входа
    path('login/', LoginView.as_view(), {'template_name': 'users/login.html'},
    name='login'),
    # Страница выхода
    path('logout/', views.logout_view, name='logout'),
    # Страница регистрации
    path('register/', views.register, name='register'),
]