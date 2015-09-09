# coding: utf-8
from __future__ import unicode_literals
from __future__ import absolute_import

from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)


class Publisher(models.Model):
    name = models.CharField(max_length=70)


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author)
    isbn = models.CharField(max_length=17)
    publisher = models.ForeignKey(Publisher)
