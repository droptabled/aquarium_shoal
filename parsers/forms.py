from django import forms
from parsers.models import Fish

class FishParserForm(forms.Form):
    fish = forms.ModelChoiceField(Fish.objects.all())
    url = forms.CharField(label='URL', max_length=255)