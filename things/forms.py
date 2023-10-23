"""Forms of the project."""
from django import forms


class ThingForm(forms.Form):
    name = forms.CharField(max_length=35)
    description = forms.CharField(widget=forms.Textarea(attrs={"maxlength": "120"}))
    quantity = forms.IntegerField(min_value=0, max_value=50, widget=forms.NumberInput())
