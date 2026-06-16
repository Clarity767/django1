from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView
from .forms import MovieForm
from .models import Movie


def home(request):
    return render(request, "movies/home.html")


def author(request):
    return render(request, "movies/author.html")


def movies(request):
    movies_list = Movie.objects.order_by("-id")
    return render(request, "movies/movies.html", {
        "movies": movies_list
    })


def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('movies')

    else:
        form = MovieForm()

    return render(request, 'movies/add_movie.html', {
        'form': form
    })


class MovieDetailView(DetailView):
    model = Movie
    template_name = "movies/movie_detail.html"
    context_object_name = "movie"


class MovieUpdateView(UpdateView):
    model = Movie
    template_name = "movies/movie_edit.html"
    fields = ["title", "director", "description", "genre", "year", "poster"]
    success_url = reverse_lazy("movies")


class MovieDeleteView(DeleteView):
    model = Movie
    template_name = "movies/movie_delete.html"
    success_url = "/movies/"