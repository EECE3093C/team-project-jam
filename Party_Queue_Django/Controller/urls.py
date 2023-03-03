from django.urls import path

from Controller.views import post_song, get_song

# URL paths for Controller app
urlpatterns = [
    path('post_song/', post_song),
    path('get_song/', get_song),
]
