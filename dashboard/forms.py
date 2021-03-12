from django import forms
from .models import CountryData


class CountryDataFrom(forms.ModelForm):
    class Meta:
        model = CountryData
        fields = '__all__'
