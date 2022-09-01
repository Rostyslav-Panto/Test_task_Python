from datetime import date
from django.contrib.auth.models import User
from django.db import models


class Portfolio(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(max_length=1200)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Image(models.Model):
    image_path = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    description = models.TextField(max_length=1200)
    portfolio_id = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    publication_date = models.DateField(default=date.today)


class Comment(models.Model):
    description = models.TextField(max_length=1200)
    image_id = models.ForeignKey(Image, on_delete=models.CASCADE)
    author_id = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    publication_date = models.DateField(default=date.today)

