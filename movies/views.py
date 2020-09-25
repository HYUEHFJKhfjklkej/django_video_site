from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Movie


class MoviesView(ListView):
    """Список аниме"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)


class MovieDetailView(DetailView):
    """Полное описание анисе"""
    model = Movie
    slug_field = "url"

class AddReview(View):
    """Отзывы"""

    def post(self, request, pk):
        print(request.POST)
        return redirect("/")