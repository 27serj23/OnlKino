from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movies_list, name='movies_list'),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
]