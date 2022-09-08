from django.db.models import (
    Model, CharField, IntegerField,
    FloatField, ForeignKey, CASCADE, Manager
)
from postgres_copy import CopyManager

from directors.models import Director


class Movie(Model):
    name = CharField(max_length=255, null=False, blank=False)
    year = IntegerField(null=False, blank=False)
    rank = FloatField(default=0, null=True)

    csv_manager = CopyManager()
    objects = Manager()


class MovieGenre(Model):
    movie = ForeignKey(Movie, on_delete=CASCADE, related_name='movie_genres')
    genre = CharField(max_length=100, null=False, blank=False)

    csv_manager = CopyManager()
    objects = Manager()


class MovieDirector(Model):
    movie = ForeignKey(Movie, on_delete=CASCADE, related_name='movie_directors')
    director = ForeignKey(Director, on_delete=CASCADE)

    csv_manager = CopyManager()
    objects = Manager()
