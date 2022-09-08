from django.urls import path

from movies.views import MovieViewSet

urlpatterns = [
    path('', MovieViewSet.as_view({'get': 'list'}), name='movies'),
]
