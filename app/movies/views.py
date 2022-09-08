from rest_framework.viewsets import ModelViewSet

from .filter import MovieFilter
from .models import Movie
from .serializers import MovieSerializer


class MovieViewSet(ModelViewSet):
    serializer_class = MovieSerializer
    filterset_class = MovieFilter

    def get_queryset(self):
        return Movie.objects.order_by('-id').all()


