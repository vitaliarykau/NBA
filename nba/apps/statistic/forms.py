from django import forms
from .models import Match, Stat



class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['date', 'time', 'team1', 'score1', 'team2', 'score2', 'arena']
        labels = {}
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control form-control-sm', 'type':'date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control form-control-sm', 'type': 'time'}),
            'team1': forms.Select(attrs={'class': 'form-control form-control-sm'}),
            'team2': forms.Select(attrs={'class': 'form-control form-control-sm'}),
            'score1': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
            'score2': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
            'arena': forms.Select(attrs={'class': 'form-control form-control-sm'}),
        }


class StatForm(forms.ModelForm):
    class Meta:
        model = Stat
        fields = ['season', 'player', 'team', 'time', 'points', 'rebounds', 'assists', 'blocks','steals' ]
        labels = {'time': 'Duration on the floor'}
        widgets = {
            'season': forms.Select(attrs={'class': 'form-control form-control-sm'}),
            'player': forms.Select(attrs={'class': 'form-control form-control-sm'}),
            'team': forms.Select(attrs={'class': 'form-control form-control-sm'}),
            'time': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'points': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
            'rebounds': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
            'assists': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
            'blocks': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
            'steals': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
        }
