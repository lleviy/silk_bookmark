from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('silk_bookmarks.urls')),
    path('account/', include("extended_account.urls")),
    path('account/', include("account.urls")),
    path('', include("unsplash_search.urls")),
]
