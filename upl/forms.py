from django import forms

choices = (('1', 'Simple CNN'),('2', 'Pretrained NN'))
class UploadDocumentForm(forms.Form):
    nn_id = forms.ChoiceField(choices=choices)
    image = forms.ImageField()