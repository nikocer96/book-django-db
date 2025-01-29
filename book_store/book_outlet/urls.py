from django.urls import path
from . import views


urlpatterns = [
    path("", views.index),
    path("<slug:slug>", views.detail_book, name="book-detail")
]
