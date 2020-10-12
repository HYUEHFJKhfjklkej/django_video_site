from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import View

from .models import Movie, Category, Hero
from .forms import ReviewForm


class MoviesView(ListView):
    """Список аниме"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    
    def get_content_data(self, *args, **kwargs):
        context = super().get_content_data(*args, **kwargs)
        context["categories"] = Category.objects.all()
        return context


class MovieDetailView(DetailView):
    """Полное описание аниме"""
    model = Movie
    slug_field = "url"


class AddReview(View):
    """Отзывы"""
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())

class HeroView(DetailView):
    """вывод информации о героях"""
    model = Hero
    template_name = 'movies/hero.html'
    slug_field = "name"
