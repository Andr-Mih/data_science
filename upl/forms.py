from django import forms

choices = (('1', 'SimpleNN'),('2', 'Pretrained'))
class UploadDocumentForm(forms.Form):
    nn_id = forms.ChoiceField(choices=choices)
    image = forms.ImageField()