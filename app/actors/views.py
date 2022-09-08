from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from actors.models import Actor
from actors.serializers import ActorSerializer


class ActorViewSet(ModelViewSet):
    serializer_class = ActorSerializer

    def get_queryset(self):
        return Actor.objects.order_by('-id').all()

    def retrieve(self, request, pk=None):
        instance = self.get_object()
        return Response(self.serializer_class(instance).data,
                        status=status.HTTP_200_OK)


