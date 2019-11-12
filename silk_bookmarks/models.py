from django.db import models
from django.contrib.auth.models import User

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
