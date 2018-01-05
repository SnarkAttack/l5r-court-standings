from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.db import IntegrityError

from ..forms.register_new_screen_name import RegisterNewScreenNameForm

from screen_name.models import ScreenName


@login_required(login_url=settings.LOGIN_URL)
def post(request):
    register_username_form = RegisterNewScreenNameForm()
    return render(request, 'register_new_name.html', {'register_form': register_username_form})


def register(request):
    if request.method == 'POST':
        form=RegisterNewScreenNameForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user_id = request.user.id
            obj.save()
            return redirect('screennames:registered_names')
        else:
            screen_name_list = ScreenName.objects.filter(screen_name=request.POST['screen_name'])
            if len(screen_name_list) is 1 and screen_name_list[0].user_id is None:
                screen_name_list.update(user_id=request.user.id)
                return redirect('screennames:registered_names')
            else:
                register_username_form = RegisterNewScreenNameForm()
                return render(request, 'register_new_name.html', {'error_message': 'ALREADY EXISTS', 'register_form': register_username_form})
