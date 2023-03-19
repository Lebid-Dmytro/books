from django.contrib import admin

from book_shop.models import Genre, Author, Book, Review, Order

admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Order)
