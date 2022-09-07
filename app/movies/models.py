from django.db.models import (
    Model, CharField, IntegerField,
    FloatField, ManyToManyField
)


class Genre(Model):
    name = CharField(max_length=100, null=False, blank=False)


class Movie(Model):
    name = CharField(max_length=255, null=False, blank=False)
    year = IntegerField(null=False, blank=False)
    rank = FloatField()

    genres = ManyToManyField(Genre)
