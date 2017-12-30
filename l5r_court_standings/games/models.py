# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Game(models.Model):
    player1 = models.IntegerField(null=True, blank=True)
    player2 = models.IntegerField(null=True, blank=True)
    player1_clan = models.IntegerField(null=True, blank=True)
    player2_clan = models.IntegerField(null=True, blank=True)
    player1_splash = models.IntegerField(null=True, blank=True)
    player2_splash = models.IntegerField(null=True, blank=True)
    # Set to false if player 1 wins, true if player 2 wins
    # Maybe there's a better way to do this
    winner = models.BooleanField()
    win_type = models.IntegerField(null=True, blank=True)
    game_date = models.DateTimeField('date played', null=True)
