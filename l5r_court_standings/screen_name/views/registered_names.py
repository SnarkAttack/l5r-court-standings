from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings

def find_registered_usernames():
    pass

@login_required(login_url=settings.LOGIN_URL)
def show_registered_names(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.id
    return render(request, 'registered_names.html')
