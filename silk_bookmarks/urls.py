"""Определяет схемы URL для silk_bookmarks."""

from django.conf.urls import url
from django.urls import path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from . import views

app_name = 'silk_bookmarks'

urlpatterns = [
    #Домашняя страница
    path('', views.index, name='index'),
    #Вывод всех книг
    path('topics/', views.topics, name='topics'),
    #Страница с подробной информацией по отдельной книге
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    #Страница для добавления отдельной книги
    path('new_topic/', views.new_topic, name='new_topic'),
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    # Страница для редактирования цитаты
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
    url(r'^del_entry/(?P<entry_id>\d+)/$', views.del_entry, name='del_entry'),
    url(r'^edit_topic/(?P<topic_id>\d+)/$', views.edit_topic, name='edit_topic'),
    url(r'^del_topic/(?P<topic_id>\d+)/$', views.del_topic, name='del_topic'),
]