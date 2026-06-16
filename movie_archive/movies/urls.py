from django.urls import path
from .views import (
    home,
    author,
    movies,
    add_movie,
    MovieDetailView,
    MovieUpdateView,
    MovieDeleteView
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('author/', author, name='author'),

    # MOVIES
    path('movies/', movies, name='movies'),
    path('movies/add/', add_movie, name='add_movie'),

    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
    path('movies/<int:pk>/edit/', MovieUpdateView.as_view(), name='movie_edit'),
    path('movies/<int:pk>/delete/', MovieDeleteView.as_view(), name='movie_delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)