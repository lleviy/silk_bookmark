from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'unsplash_search'

urlpatterns = [
    # url для поиска картинок по запросу пользователя(данный url содержит Json-ответ)
    url(r'search_photos/$', views.search_photos, name='search_photos'),
]