from django.urls import path

from actors.views import ActorViewSet

urlpatterns = [
    path('', ActorViewSet.as_view({'get': 'list'}), name='actors'),
    path('<int:pk>/', ActorViewSet.as_view({'get': 'retrieve'}), name='actors'),
]
