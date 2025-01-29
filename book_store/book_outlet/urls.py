from django.urls import path
from . import views


urlpatterns = [
    path("", views.index),
    path("<int:id>", views.detail_book, name="book-detail")
]
