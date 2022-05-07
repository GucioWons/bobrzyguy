from django import forms
from django.forms import ModelForm

from Team.models import Team


class CreateTeamForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'type': 'text'}))
    description = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Team
        fields = ('name', 'description')