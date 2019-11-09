from django.shortcuts import render

from django.http import HttpResponseRedirect, Http404, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

from unsplash_search.views import search_photos_default

def generate_random_quote(request):
    '''Генерирует случайную цитату из добавленных пользователем'''
    random_quote = ''
    if Topic.objects.filter(owner = request.user).count():
            random_book = Topic.objects.filter(owner=request.user).order_by('?')[:1][0]
            if random_book.entry_set.count() > 0:
                random_quote = random_book.entry_set.order_by('?')[:1][0]
            else:
                random_book = ''
    return random_quote, random_book

def index(request):
    """Домашняя страница приложения silk_bookmarks"""
    context = {}
    if request.user.is_authenticated:
        random_quote, random_book = generate_random_quote(request)
        context = {'quote': random_quote, 'topic': random_book}
    return render(request, 'silk_bookmarks/index.html', context)

def check_topic_owner(request, owner):
    '''Проверяет, является ли текущий пользователь создателем запрашиваемого объекта'''
    if owner != request.user:
        raise Http404

@login_required
def topics(request):
    """Выводит список книг."""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'silk_bookmarks/topics.html', context)

@login_required
def topic(request, topic_id):
    """Выводит информацию и цитаты по конкретной книге."""
    topic = Topic.objects.get(id=topic_id)
    author = topic.author
    status = topic.status
    adv = topic.adv
    assoc = topic.assoc
    check_topic_owner(request, topic.owner)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'author': author, 'entries': entries, 'status': status, 'adv': adv, 'assoc': assoc}
    return render(request, 'silk_bookmarks/topic.html', context)

@login_required
def new_topic(request):
    """Определяет новую книгу"""
    photos_url = search_photos_default()
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = TopicForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = TopicForm(request.POST, request.FILES)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('silk_bookmarks:topics'))
    context = {'form': form, 'photos_url': photos_url}
    return render(request, 'silk_bookmarks/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Добавляет новую цитату к конкретной книге."""
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(request, topic.owner)
    if request.method != 'POST':
    # Данные не отправлялись; создается пустая форма.
        form = EntryForm()
    else:
    # Отправлены данные POST; обработать данные.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('silk_bookmarks:topic',
            args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'silk_bookmarks/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Редактирует существующую цитату к конкретной книге."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    topic_id = topic.id
    check_topic_owner(request, topic.owner)
    if request.method != 'POST':
        # Данные не отправлялись; форма заполняется данными текущей записи.
        form = EntryForm(instance=entry)
    else:
        # Отправлены данные POST; обработать данные.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('silk_bookmarks:topic', 
            args=[topic_id]))
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'silk_bookmarks/edit_entry.html', context)

@login_required
def edit_topic(request, topic_id):
    photos_url = search_photos_default()
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(request, topic.owner)
    if request.method != 'POST':
        # Данные не отправлялись; форма заполняется данными текущей записи.
        form = TopicForm(instance=topic)
    else:
        form = TopicForm(data=request.POST, files=request.FILES, instance=topic)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('silk_bookmarks:topic', 
            args=[topic_id]))
    context = {'topic': topic, 'form': form, 'photos_url': photos_url}
    return render(request, 'silk_bookmarks/edit_topic.html', context)

@login_required
def del_topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(request, topic.owner)
    topic.delete()
    return HttpResponseRedirect(reverse('silk_bookmarks:topics'))

@login_required
def del_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    topic_id = topic.id
    check_topic_owner(request, topic.owner)
    entry.delete()
    return HttpResponseRedirect(reverse('silk_bookmarks:topic',
            args=[topic_id]))
