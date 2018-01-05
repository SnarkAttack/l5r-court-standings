from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings

from games.models import Game
from screen_name.models import ScreenName

def find_registered_usernames():
    pass

@login_required(login_url=settings.LOGIN_URL)
def show_recorded_games(request):
    game_list = Game.objects.order_by('-game_date')[:10]
    # if request.user.is_authenticated():
    #     username = request.user.id
    for game in game_list:
        game.player1 = ScreenName.get_name_from_id(game.player1)
        game.player2 = ScreenName.get_name_from_id(game.player2)
        game.winner = 'Win' if game.winner else 'Loss'
    return render(request, 'game_display.html', {'game_details_list': game_list})
