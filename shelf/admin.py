# coding: utf-8
from __future__ import unicode_literals
from __future__ import absolute_import

from django.contrib import admin
from .models import Author, Publisher, Book

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['last_name', 'first_name']
    ordering = ['last_name']

class BookAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'author', 'isbn', 'publisher']

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)

admin.site.register(Publisher)
