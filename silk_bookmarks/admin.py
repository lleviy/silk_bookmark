from django.contrib import admin

# Register your models here.
from silk_bookmarks.models import Book, Quote

admin.site.register(Book)
admin.site.register(Quote)