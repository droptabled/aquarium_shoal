from django import forms

class FishForm(forms.Form):
    scientific_name = forms.CharField(label='Scientific Name', max_length=100)
    common_names = forms.CharField(label='Common Names (comma delimited)')