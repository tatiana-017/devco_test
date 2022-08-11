from django import forms

class contactForm(forms.Form):
    requestName = forms.CharField(label="Nombre", required= True)
    requestEmail = forms.EmailField(label="Email", required=True)
    requestCont = forms.CharField(label='Mensaje', widget=forms.Textarea)