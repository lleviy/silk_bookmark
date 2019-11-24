from django.db import models
from django.contrib.auth.models import User
from django.forms.models import modelform_factory
from django.conf import settings

from django.core.files.storage import get_storage_class


# class S3PrivateImageField(models.ImageField):
#     """
#     A ImageField that gives the 'private' ACL to the files it uploads to S3, instead of the default ACL.
#     """
#     def __init__(self, verbose_name=None, name=None, upload_to='', storage=None, **kwargs):
#         if storage is None:
#             storage = get_storage_class()(acl='private')
#         super(S3PrivateImageField, self).__init__(verbose_name=verbose_name,
#                 name=name, upload_to=upload_to, storage=storage, **kwargs)

class Topic(models.Model):
    """Тема, которую изучает пользователь"""
    text = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    STATUSES = (
        ('read', 'read'),
        ('currently reading', 'currently reading'),
        ('not read', 'not read'),
    )
    status = models.CharField(max_length=17, choices=STATUSES)
    adv = models.TextField(max_length=400, blank=True)
    assoc = models.CharField(max_length=100, blank=True)
    photo_url = models.URLField(blank=True)

    def __str__(self):
        """Возвращает строковое представление модели."""
        return self.text

# class Group(models.Model):
#     """Группа, в которую пользователь объединяет книги"""
#     text = models.CharField(max_length=50)
#     owner = models.ForeignKey(User, on_delete=models.CASCADE)
#     def __str__(self):
#         """Возвращает строковое представление модели."""
#         return self.text


class Entry(models.Model):
    """Информация, изученная пользователем по теме"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        """Возвращает строковое представление модели."""
        if len(self.text) < 50:
            return self.text
        return self.text[:50] + "..."
