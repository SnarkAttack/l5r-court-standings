# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from screen_name.models import ScreenName

class Game(models.Model):
    player1 = models.IntegerField(null=True, blank=True)
    player2 = models.IntegerField(null=True, blank=True)
    player1_clan = models.IntegerField(null=True, blank=True)
    player2_clan = models.IntegerField(null=True, blank=True)
    player1_splash = models.IntegerField(null=True, blank=True)
    player2_splash = models.IntegerField(null=True, blank=True)
    # Set to True if player 1 wins, False if player 2 wins
    winner = models.BooleanField()
    win_type = models.IntegerField(null=True, blank=True)
    game_date = models.DateTimeField('date played', null=True)

    @classmethod
    def obj_from_json(cls, post_request, date):
        player = None
        opponent = None
        try:
            opponent = ScreenName.objects.get(screen_name=post_request['opponent_username'])
        except ScreenName.DoesNotExist:
            new_user = ScreenName(user_id=None, screen_name=post_request['opponent_username'])
            new_user.save()
            opponent = new_user

        g = Game(player1=post_request['player_id'], player2=opponent.id, player1_clan=post_request['player_clan'],
            player1_splash=post_request['player_splash'], player2_clan=post_request['opponent_clan'],
            player2_splash=post_request['opponent_splash'], winner=post_request['win'],
            win_type=post_request['win_type'], game_date=date)

        g.save()
