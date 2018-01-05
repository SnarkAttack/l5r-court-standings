from django.conf.urls import url

from .views import show_recorded_games, record_game

urlpatterns = [
    url(r'^$', show_recorded_games.show_recorded_games, name='display_games'),
    url(r'^record/', record_game.post, name='new_game'),
    url(r'^save_game/', record_game.save_game, name='save_game')
]
