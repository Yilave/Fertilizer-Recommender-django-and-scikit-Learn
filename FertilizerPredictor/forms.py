from django import forms
from .models import Data
from django.contrib.auth.forms import UserCreationForm

class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        exclude = ['user', 'chart_type',]




class ChartChoiceForm(forms.ModelForm):

    class Meta:
        model = Data
        fields = ('chart_type',)