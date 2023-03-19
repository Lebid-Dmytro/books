from django.contrib.auth.models import User
from django.db import models


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=13)
    full_address = models.CharField(max_length=100)

    def __str__(self):
        return f'Юзер: {self.user}'
