from django.urls import path
from . import views

urlpatterns = [    
    path("movies/<int:movie_id>/", views.MovieDetailView.as_view()),
    path("movies/", views.MovieView.as_view()),
]
