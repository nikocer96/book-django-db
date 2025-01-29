from django.shortcuts import render
from django.http import Http404
from .models import Book
# Create your views here.

def index(request):
    books = Book.objects.all()
    return render(request, "book_outlet/index.html", {
        "books": books
    })
    
def detail_book(request, id):
    try:
        book = Book.objects.get(pk = id)
    except:
        raise Http404("not found")
    return render(request, "book_outlet/book_detail.html", {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestselling": book.is_bestselling
    })