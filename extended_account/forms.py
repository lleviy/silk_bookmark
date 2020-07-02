from django import forms

from .models import Appearance

from account.forms import SettingsForm


class AppearanceForm(forms.ModelForm):
    class Meta:
        model = Appearance
        fields = ['photo_url']
        labels = {'photo_url': 'photo'}
        widgets = {'photo_url': forms.HiddenInput()}


class SettingsForm(SettingsForm):
    timezone = forms.ChoiceField(
        widget=forms.HiddenInput()
    )
    language = forms.ChoiceField(
        widget=forms.HiddenInput()
    )