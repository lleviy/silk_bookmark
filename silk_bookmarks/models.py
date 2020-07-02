from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
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


class Quote(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'quotes'

    def __str__(self):
        """Возвращает строковое представление модели."""
        if len(self.text) < 50:
            return self.text
        return self.text[:50] + "..."
