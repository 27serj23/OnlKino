from django.shortcuts import render
from .models import Movie


def movies_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies_list.html', {'movies': movies})


def movie_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'movie_detail.html', {'movie': movie})