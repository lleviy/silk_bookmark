from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'extended_account'

urlpatterns = [
    url(r"^settings/$", views.SettingsView.as_view(), name='account_settings'),
    path('settings/appearance/', views.AppearanceView.as_view(), name='account_appearance'),
    # path('settings/appearance/', views.new_appearance, name='account_appearance'),
    ]