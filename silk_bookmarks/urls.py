"""Определяет схемы URL для silk_bookmarks."""

from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'silk_bookmarks'

urlpatterns = [
    #Домашняя страница
    path('', views.index, name='index'),
    #Вывод всех книг
    path('books/', views.books, name='books'),
    #Страница с подробной информацией по отдельной книге
    url(r'^books/(?P<book_id>\d+)/$', views.book, name='book'),
    #Страница для добавления отдельной книги
    path('new_book/', views.new_book, name='new_book'),
    #Страница для добавления цитаты к книге
    url(r'^new_quote/(?P<book_id>\d+)/$', views.new_quote, name='new_quote'),
    # Страница для редактирования цитаты
    url(r'^edit_quote/(?P<quote_id>\d+)/$', views.edit_quote, name='edit_quote'),
    url(r'^del_quote/(?P<quote_id>\d+)/$', views.del_quote, name='del_quote'),
    url(r'^edit_book/(?P<book_id>\d+)/$', views.edit_book, name='edit_book'),
    url(r'^del_book/(?P<book_id>\d+)/$', views.del_book, name='del_book'),
    ]