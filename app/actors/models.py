from django.db.models import (
    Model, CharField, ForeignKey, CASCADE
)

from movies.models import Movie

GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
    )


class Actor(Model):
    first_name = CharField(max_length=100, null=False, blank=False)
    last_name = CharField(max_length=100, null=False, blank=False)
    gender = CharField(max_length=1, choices=GENDERS)


class Role(Model):
    role = CharField(max_length=100, null=False, blank=False)
    actor = ForeignKey(Actor, on_delete=CASCADE)
    movie = ForeignKey(Movie, on_delete=CASCADE)

