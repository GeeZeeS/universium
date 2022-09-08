from django.db.models import (
    Model, CharField, ForeignKey, CASCADE, Manager, Count
)
from postgres_copy import CopyManager

from movies.models import Movie, MovieGenre

GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
    )


class Actor(Model):
    first_name = CharField(max_length=100, null=False, blank=False)
    last_name = CharField(max_length=100, null=False, blank=False)
    gender = CharField(max_length=1, choices=GENDERS)

    csv_manager = CopyManager()
    objects = Manager()

    def number_of_movies(self):
        return Movie.objects.filter(
            role__actor_id=self.pk
        ).all().count()

    def top_genres(self):
        movie_genre = MovieGenre.objects.values('genre').filter(
            movie__role__actor_id=self.pk
        ).annotate(count=Count('genre')).order_by('-count').first()
        return movie_genre['genre'] if movie_genre else None

    def number_of_movies_by_genre(self):
        movie_genres = MovieGenre.objects.values('genre').filter(
            movie__role__actor_id=self.pk
        ).annotate(count=Count('genre')).order_by('-count')
        return [{movie_genre['genre']: movie_genre['count'] for movie_genre in movie_genres}]

    def most_frequent_partner(self):
        movie_id_list = Movie.objects.filter(role__actor_id=self.pk).values_list('id', flat=True)
        partner = Actor.objects.filter(
            actor_roles__movie_id__in=movie_id_list
        ).annotate(count=Count('actor_roles__actor')).order_by('-count')
        if partner.count() == 1:
            return None
        return {
            "partner_actor_id": partner[1].id,
            "partner_actor_name": f"{partner[1].first_name} {partner[1].last_name}",
            "number_of_shared_movies": partner[1].count
        }


class Role(Model):
    actor = ForeignKey(Actor, on_delete=CASCADE, related_name='actor_roles')
    movie = ForeignKey(Movie, on_delete=CASCADE)
    role = CharField(max_length=100, null=False, blank=False)

    csv_manager = CopyManager()
    objects = Manager()

