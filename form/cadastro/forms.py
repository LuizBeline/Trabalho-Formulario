# -*- coding: utf-8 -*-
from django import forms
from cadastro.models import Inscricao

class InscricaoForm(forms.ModelForm):
    
    nome = forms.CharField(max_length=300)
    tipo_pessoa = forms.CharField(max_length=100)
    cpf_cnpj = forms.CharField('cpf_cnpj', max_length=20, unique=True)
    rg = forms.CharField(max_length=25, unique=True)
    idade = forms.IntegerField()
    email = forms.EmailField(unique=True)
    telefone = forms.CharField(max_length=20, blank=True)
    criado_em = forms.DateTimeField('criado em', auto_now_add=True)
    
class Meta:
     forms = Inscricao