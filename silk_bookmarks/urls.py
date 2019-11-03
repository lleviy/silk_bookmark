"""Определяет схемы URL для silk_bookmarks."""

from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'silk_bookmarks'

# urlpatterns = [
#     #Домашняя страница
#     url('^$', views.index, name='index'),
#     #Вывод всех тем
#     url('^topics/$', views.topics, name='topics'),
# ]

urlpatterns = [
    #Домашняя страница
    path('', views.index, name='index'),
    #Вывод всех тем
    path('topics/', views.topics, name='topics'),
    #Страница с подробной информацией по отдельной теме
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    #Страница для добавления отдельной темы
    path('new_topic/', views.new_topic, name='new_topic'),
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    # Страница для редактирования записи
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
    url(r'^del_entry/(?P<entry_id>\d+)/$', views.del_entry, name='del_entry'),
    url(r'^edit_topic/(?P<topic_id>\d+)/$', views.edit_topic, name='edit_topic'),
    url(r'^del_topic/(?P<topic_id>\d+)/$', views.del_topic, name='del_topic'),
]