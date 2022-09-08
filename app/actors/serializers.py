from rest_framework.serializers import ModelSerializer

from actors.models import Actor


class ActorSerializer(ModelSerializer):
    class Meta:
        model = Actor
        fields = (
            'id', 'first_name', 'last_name', 'gender',
            'number_of_movies', 'top_genres', 'number_of_movies_by_genre',
            'most_frequent_partner'
        )

