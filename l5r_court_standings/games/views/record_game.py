from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.db import IntegrityError

from ..forms.manual_game_form import ManualRecordGameForm

from games.models import Game

from datetime import datetime

from time import gmtime, mktime

@login_required(login_url=settings.LOGIN_URL)
def post(request):
    record_game_form = ManualRecordGameForm(player_id=request.user.id)
    return render(request, 'record_game.html', {'record_form': record_game_form})

@login_required(login_url=settings.LOGIN_URL)
def save_game(request):
    if request.method == 'POST':
        data = request.POST

        #date = datetime.fromtimestamp(mktime(gmtime()))

        Game.obj_from_json(data, datetime.utcnow())


    return redirect('games:display_games')
