from django.shortcuts import render
from books.models import Book
from django.core.paginator import Paginator
from datetime import datetime


def catalog(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {'books': books}
    return render(request, template, context)


def books_view(request, pub_date: datetime):
    template = 'books/books_list.html'
    books = Book.objects.filter(pub_date=pub_date)
    prev_date = Book.objects.filter(pub_date__lt=pub_date).values('pub_date').first()
    next_date = Book.objects.filter(pub_date__gt=pub_date).values('pub_date').first()
    paginator = Paginator(books, 10)
    page = paginator.get_page(pub_date)
    if not prev_date:
        context = {
            'books': page,
            'next': str(next_date['pub_date']),
        }
    elif not next_date:
        context = {
            'books': page,
            'prev': str(prev_date['pub_date']),
        }
    else:
        context = {
            'books': page,
            'prev': str(prev_date['pub_date']),
            'next': str(next_date['pub_date']),
        }
    return render(request, template, context)
