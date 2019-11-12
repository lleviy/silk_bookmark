from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text', 'author', 'status', 'assoc', 'adv']
        labels = {'text': 'title', 'author': 'author', 'status': 'status', 'adv': '* review or your thoughts and feelings', 
        'assoc': '* associations: several keywords, may be mood or genre'
        }

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
