from django import forms

class emp(forms.Form):
    name=forms.CharField(max_length=100)
    address=forms.CharField(max_length=100)
    text=forms.CharField(widget=forms.Textarea)