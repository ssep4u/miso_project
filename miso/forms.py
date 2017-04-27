from django import forms
from django.forms import ModelForm
from .models import Word

class WordForm(forms.Form):
    word = forms.CharField(label='word', max_length=10)
