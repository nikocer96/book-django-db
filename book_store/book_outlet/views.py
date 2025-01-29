from django.shortcuts import render
from django.http import Http404
from .models import Book
from django.db.models import Avg
# Create your views here.

def index(request):
    books = Book.objects.all().order_by("author")
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))
    return render(request, "book_outlet/index.html", {
        "books": books,
        "num_books": num_books,
        "avg_rating": avg_rating
    })
    
def detail_book(request, slug):
    try:
        book = Book.objects.get(slug = slug)
    except:
        raise Http404("not found")
    return render(request, "book_outlet/book_detail.html", {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestselling": book.is_bestselling
    })