from django.db.models import fields
from django.db.models.base import Model
from django.forms import ModelForm, widgets
from app.models import Orcamentos, Carros, Vendedores
from django import forms
from .models import *

class OrcamentosForm(ModelForm):
    class Meta:
        model = Orcamentos
        fields = ['quantidade', 'descricao', 'precoUnitario', 'subTotal', 'total', 'frete', 'taxas']

        widgets = {
            'quantidade':forms.TextInput(attrs={'class':'form-control'}),
            'descricao':forms.TextInput(attrs={'class':'form-control'}),
            'precoUnitario':forms.TextInput(attrs={'class':'form-control'}),
            'subTotal':forms.TextInput(attrs={'class':'form-control'}),
            'total':forms.TextInput(attrs={'class':'form-control'}),
            'frete':forms.TextInput(attrs={'class':'form-control'}),
            'taxas':forms.TextInput(attrs={'class':'form-control'}),
            
        }


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