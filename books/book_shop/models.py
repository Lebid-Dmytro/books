from django.db import models
from django.template.defaultfilters import slugify

from client.models import Client


class Genre(models.Model):
    """Категорія"""
    name = models.CharField(max_length=150)
    url = models.SlugField(max_length=130)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.url = slugify(self.name)
        super(Genre, self).save(*args, **kwargs)


class Author(models.Model):
    """Автор"""
    name = models.CharField(max_length=100)
    year_born = models.PositiveSmallIntegerField(default=0)
    year_dead = models.PositiveSmallIntegerField(default=0)
    history_life = models.TextField()
    image = models.ImageField(upload_to="media/authors/")
    url = models.SlugField(max_length=130)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.url = slugify(self.name)
        super(Author, self).save(*args, **kwargs)


class Book(models.Model):
    """Книга"""
    title = models.CharField(max_length=100)
    description = models.TextField()
    poster = models.ImageField(upload_to="media/books/")
    year = models.PositiveSmallIntegerField(default=2000)
    country = models.CharField(max_length=30)
    directors = models.ManyToManyField(Author, related_name="author")
    genres = models.ManyToManyField(Genre)
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.url = slugify(self.title)
        super(Book, self).save(*args, **kwargs)


class Review(models.Model):
    """Відгуки"""
    email = models.EmailField()
    name = models.CharField(max_length=100)
    text = models.TextField(max_length=5000)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")

    def __str__(self):
        return f"{self.name} - {self.book}"


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="orders")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="books")
