from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings

from screen_name.models import ScreenName

def find_registered_usernames():
    pass

@login_required(login_url=settings.LOGIN_URL)
def show_registered_names(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.id
    return render(request, 'registered_names.html')

def get_registered_names(player_id):
    user_screen_names = ScreenName.objects.filter(user_id=player_id)
    formatted_list = []
    for name in user_screen_names:
        formatted_list.append((name.id, name.screen_name))
    print formatted_list
    return formatted_list
