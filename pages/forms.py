from django import forms

class FishForm(forms.Form):
    fish_name = forms.CharField(label='Fish Name', max_length=100)