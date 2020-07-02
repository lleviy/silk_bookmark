from django.shortcuts import render

from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Book, Quote
from .forms import BookForm, QuoteForm

from unsplash_search.views import search_photos_default
from extended_account.models import Appearance


def generate_random_quote(request):
    random_quote = ''
    random_book = ''
    if Book.objects.filter(owner = request.user).count():
            random_book = Book.objects.filter(owner=request.user).order_by('?')[:1][0]
            if random_book.quote_set.count() > 0:
                random_quote = random_book.quote_set.order_by('?')[:1][0]
            else:
                random_book = ''
    return random_quote, random_book

def index(request):
    context = {}
    if request.user.is_authenticated:
        random_quote, random_book = generate_random_quote(request)
        appearance = Appearance.objects.filter(owner=request.user)[0]
        context = {'quote': random_quote, 'book': random_book, 'appearance': appearance}
    return render(request, 'silk_bookmarks/index.html', context)

def check_book_owner(request, owner):
    if owner != request.user:
        raise Http404

@login_required
def books(request):
    books = Book.objects.filter(owner=request.user).order_by('-date_added')
    appearance = Appearance.objects.filter(owner=request.user)[0]
    context = {'books': books, 'appearance': appearance}
    return render(request, 'silk_bookmarks/books.html', context)

@login_required
def book(request, book_id):
    book = Book.objects.get(id=book_id)
    author = book.author
    status = book.status
    adv = book.adv
    assoc = book.assoc
    check_book_owner(request, book.owner)
    quotes = book.quote_set.order_by('-date_added')
    context = {'book': book, 'author': author, 'quotes': quotes, 'status': status, 'adv': adv, 'assoc': assoc}
    return render(request, 'silk_bookmarks/book.html', context)

@login_required
def new_book(request):
    photos_url = search_photos_default()
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = BookForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            new_book = form.save(commit=False)
            new_book.owner = request.user
            new_book.save()
            return HttpResponseRedirect(reverse('silk_bookmarks:books'))
    context = {'form': form, 'photos_url': photos_url}
    return render(request, 'silk_bookmarks/new_book.html', context)

@login_required
def new_quote(request, book_id):
    book = Book.objects.get(id=book_id)
    check_book_owner(request, book.owner)
    if request.method != 'POST':
    # Данные не отправлялись; создается пустая форма.
        form = QuoteForm()
    else:
    # Отправлены данные POST; обработать данные.
        form = QuoteForm(data=request.POST)
        if form.is_valid():
            new_quote = form.save(commit=False)
            new_quote.book = book
            new_quote.save()
            return HttpResponseRedirect(reverse('silk_bookmarks:book',
            args=[book_id]))
    context = {'book': book, 'form': form}
    return render(request, 'silk_bookmarks/new_quote.html', context)

@login_required
def edit_quote(request, quote_id):
    quote = Quote.objects.get(id=quote_id)
    book = quote.book
    book_id = book.id
    check_book_owner(request, book.owner)
    if request.method != 'POST':
        # Данные не отправлялись; форма заполняется данными текущей записи.
        form = QuoteForm(instance=quote)
    else:
        # Отправлены данные POST; обработать данные.
        form = QuoteForm(instance=quote, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('silk_bookmarks:book',
            args=[book_id]))
    context = {'quote': quote, 'book': book, 'form': form}
    return render(request, 'silk_bookmarks/edit_quote.html', context)

@login_required
def edit_book(request, book_id):
    photos_url = search_photos_default()
    book = Book.objects.get(id=book_id)
    check_book_owner(request, book.owner)
    if request.method != 'POST':
        # Данные не отправлялись; форма заполняется данными текущей записи.
        form = BookForm(instance=book)
    else:
        form = BookForm(data=request.POST, files=request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('silk_bookmarks:book',
                                                args=[book_id]))
    context = {'book': book, 'form': form, 'photos_url': photos_url}
    return render(request, 'silk_bookmarks/edit_book.html', context)

@login_required
def del_book(request, book_id):
    book = Book.objects.get(id=book_id)
    check_book_owner(request, book.owner)
    book.delete()
    return HttpResponseRedirect(reverse('silk_bookmarks:books'))

@login_required
def del_quote(request, book_id):
    quote = Quote.objects.get(id=quote_id)
    book = quote.book
    book_id = book.id
    check_book_owner(request, book.owner)
    quote.delete()
    return HttpResponseRedirect(reverse('silk_bookmarks:book',
            args=[book_id]))