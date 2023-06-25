from django import forms

class FishParserForm(forms.Form):
    fish = forms.CharField(label='Fish Name', max_length=100)
    url = forms.CharField(label='URL', max_length=255)