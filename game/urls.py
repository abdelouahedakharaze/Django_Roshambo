from django.urls import path
from .views import play_game

urlpatterns = [
    path('', play_game, name='play_game'),
]
