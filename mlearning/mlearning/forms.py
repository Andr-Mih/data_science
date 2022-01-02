from django import forms
from django.forms.fields import ImageField

class NameForm(forms.Form):
    image = ImageField()


