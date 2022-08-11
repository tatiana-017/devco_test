from django.forms import ModelForm
from django import forms
from .models import assing

class assingForm(ModelForm):
    serial = forms.IntegerField(label="Serial del dispositivo", required = True)
    name = forms.CharField(label="Nombre del producto", required= True)
    typeProduct = forms.CharField(label="Tipo de producto", required= True)
    system = forms.CharField(label="Sistema operativo")
    ownerName = forms.CharField(label="Nombre del propietario", required=True)
    ownerEmail = forms.EmailField(label="Email del propietario", required=True)
    date = forms.DateField(label="Fecha de asignación", required=True)

    class Meta:
        model = assing
        fields = ['serial','name','typeProduct','system',
        'ownerName','ownerEmail','date']
