from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'unsplash_search'

urlpatterns = [
    # url для поиска картинок по запросу пользователя(данный url содержит Json-ответ)
<<<<<<< HEAD
    url(r'search_photos/$', views.search_photos, name='search_photos'),
=======
    url(r'/search_photos/$', views.search_photos, name='search_photos'),
>>>>>>> ce337d430a5f020493aca6dd7083b8e625deff0a
]