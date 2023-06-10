from django import forms
from .models import User

# Criando o 'modelForm:'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nome', 'telefone', 'email']
        