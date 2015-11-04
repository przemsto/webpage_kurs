# coding: utf-8
from __future__ import unicode_literals
from __future__ import absolute_import

from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Author

class AuthorListView(ListView):
    model = Author

class AuthorDetailView(DetailView):
    model = Author

