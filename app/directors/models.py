from django.db.models import Model, CharField, FloatField, ForeignKey, CASCADE, Manager
from postgres_copy import CopyManager


class Director(Model):
    first_name = CharField(max_length=100, null=False)
    last_name = CharField(max_length=100, blank=False)

    csv_manager = CopyManager()
    objects = Manager()


class DirectorGenre(Model):
    director = ForeignKey(Director, on_delete=CASCADE)
    genre = CharField(max_length=50, null=False)
    prob = FloatField(null=False)

    csv_manager = CopyManager()
    objects = Manager()
