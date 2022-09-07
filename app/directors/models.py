from django.db.models import Model, CharField, ManyToManyField

from movies.models import Movie


class Director(Model):
    first_name = CharField(max_length=100, null=False)
    last_name = CharField(max_length=100, blank=False)

    movies = ManyToManyField(Movie)
