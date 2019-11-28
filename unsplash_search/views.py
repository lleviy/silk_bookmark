from django.shortcuts import render

from django.http import JsonResponse

from .api import unsplash_api
from unsplash.errors import UnsplashError

def search_photos(request, topic_id = None):
    '''Cлучайная генерация 12 фотографий Unsplash в соответствии с пользовательским запросом'''
    if request.method == 'GET':
        q = request.GET.get('q')
        photos_url = []
        try:
            search = unsplash_api.photo.random(orientation='landscape', count=12, query=q)
        except UnsplashError:
            return render(request, 'silk_bookmarks/new_topic.html', {})
        else:
            for photo in search:
                photos_url.append(f'https://source.unsplash.com/{photo.id}/1600x900')
            return JsonResponse({'photos_url':photos_url}, safe=False)
    return JsonResponse({},safe=False)

def search_photos_default():
    '''Cлучайная генерация 12 фотографий Unsplash из определенной коллекции (нейтральные настроения)'''
    photos_url = []
    search = unsplash_api.photo.random(orientation='landscape', count=12, collections='983862')
    for photo in search:
        photos_url.append(f'https://source.unsplash.com/{photo.id}/1600x900')
    return photos_url
