from django.db import models
from rest_framework import generics, viewsets

from book_shop.models import Author, Book
from book_shop.serializers import (
    BookSerializer,
    BookDetailSerializer,
    ReviewSerializer,
    AuthorSerializer,
    AuthorDetailSerializer,
    CreateRatingSerializer
)
from book_shop.service import get_client_ip


class BookListView(generics.ListAPIView):
    '''Список книг'''
    serializer_class = BookSerializer

    def get_queryset(self):
        books = Book.objects.filter(draft=True).annotate(
            rating_user=models.Count("ratings",
                                     filter=models.Q(ratings__ip=get_client_ip(self.request)))
        ).annotate(
            middle_star=models.Sum(models.F('ratings__star')) / models.Count(models.F('ratings'))
        )
        return books
    #
    # def get_queryset(self):
    #     books = Book.objects.filter(draft=True)
    #     return books


class BookDetailView(generics.RetrieveAPIView):
    '''Деталі про книгу'''
    queryset = Book.objects.filter(draft=True)
    serializer_class = BookDetailSerializer


class ReviewView(generics.CreateAPIView):
    '''Залишити відгук'''
    serializer_class = ReviewSerializer


class AuthorListView(generics.ListAPIView):
    '''Автори'''
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetailView(generics.ListAPIView):
    '''Деталі про автора'''
    queryset = Author.objects.all()
    serializer_class = AuthorDetailSerializer


class AddStarRatingViewSet(generics.CreateAPIView):
    '''Додати/змінити зірки руйтингу до книги'''
    serializer_class = CreateRatingSerializer

    def perform_create(self, serializer):
        serializer.save(ip=get_client_ip(self.request))

