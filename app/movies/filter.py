from django.db.models import Q
from django_filters.rest_framework import CharFilter, FilterSet

from .models import Movie


class MovieFilter(FilterSet):
    director = CharFilter(method='filter_director', field_name='movie_directors')
    genre = CharFilter(method='filter_genre', field_name='movie_genres')

    class Meta:
        model = Movie
        fields = ('director', 'genre')

    def filter_director(self, queryset, field_name, value):
        return queryset.filter(
            Q(movie_directors__director__first_name__icontains=value
              ) | Q(movie_directors__director__last_name__icontains=value)
        ).distinct()

    def filter_genre(self, queryset, field_name, value):
        return queryset.filter(
            movie_genres__genre__icontains=value
        ).distinct()
