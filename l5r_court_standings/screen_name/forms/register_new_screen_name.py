from django import forms
from django.forms import ModelForm
from ..models import ScreenName

class RegisterNewScreenNameForm(ModelForm):
    class Meta:
        model = ScreenName
        fields = ('screen_name',)
