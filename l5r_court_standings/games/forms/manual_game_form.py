from django import forms
from ..models import Game
from games.api.translations.clans import get_clans_list
from screen_name.views.registered_names import get_registered_names

class ManualRecordGameForm(forms.Form):

    def __init__(self, *args, **kwargs):
        player_id = kwargs.pop('player_id')
        super(ManualRecordGameForm, self).__init__(*args, **kwargs)

        self.fields['player_id'] = forms.ChoiceField(choices=get_registered_names(player_id))

    player_id = forms.ChoiceField(choices=[(0, '---')])
    opponent_username = forms.CharField(required=False)
    player_clan = forms.ChoiceField(choices=get_clans_list())
    player_splash = forms.ChoiceField(choices=get_clans_list())
    opponent_clan = forms.ChoiceField(choices=get_clans_list())
    opponent_splash = forms.ChoiceField(choices=get_clans_list())
    win = forms.ChoiceField(choices=[(True, 'Player'), (False, 'Opponent')])
    win_type = forms.ChoiceField(choices=[(0, 'Stronghold break'), (1, 'Honor'), (2, 'Dishonor'), (3, 'Concede')])
    # Just want to fill in for based on time entered
