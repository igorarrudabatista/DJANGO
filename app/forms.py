from django.forms import ModelForm
from app.models import Carros, Vendedores
from django import forms
from .models import *


class CarrosForm(ModelForm):
    class Meta:
        model = Carros
        fields = ['modelo', 'marca', 'ano', 'image']

        widgets = {
            'modelo':forms.TextInput(attrs={'class':'form-control'}),
            'marca': forms.TextInput(attrs={'class':'form-control'}),
            'ano':   forms.TextInput(attrs={'class':'form-control'})
           
    
           }



class VendedoresForm(ModelForm):
    class Meta:
        model = Vendedores
        fields = ['nome', 'telefone', 'nascimento', 'endereco', 'funcao', 
        'estado', 'cidade', 'cep', 'rua', 'foto']

        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'telefone': forms.TextInput(attrs={'class':'form-control'}),
            'nascimento': forms.TextInput(attrs={'class':'form-control default-date-picker form-control-inline ' , 'placeholder': 'dd/mm/aaaa'}),
            'endereco': forms.TextInput(attrs={'class':'form-control'}),
            'funcao': forms.TextInput(attrs={'class':'form-control'}),
            'estado': forms.TextInput(attrs={'class':'form-control'}),
            'cidade': forms.TextInput(attrs={'class':'form-control'}),
            'cep': forms.TextInput(attrs={'class':'form-control'}),
            'rua': forms.TextInput(attrs={'class':'form-control'}),
            
    
           }