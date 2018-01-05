# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class ScreenNameManager(models.Manager):
    def register_screen_name(self, screen_name, user_id):
        new_username = self.get_or_create(screen_name=jinteki_username, user_id=site_username)
        return new_username

class ScreenName(models.Model):
    user_id = models.IntegerField(null=True)
    screen_name = models.CharField(max_length=32, unique=True)

    objects = ScreenNameManager()

    @classmethod
    def get_name_from_id(cls, id):
        name_obj = ScreenName.objects.get(id=id)
        return name_obj.screen_name
