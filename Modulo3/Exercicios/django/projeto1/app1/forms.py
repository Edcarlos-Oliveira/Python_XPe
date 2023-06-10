# Importando a biblioteca de formulários do django
# Importando dados do .models e User do app1

from django import forms
from .models import User

# Tipo de formulários 'modelForm':

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nome', 'telefone', 'email']

# Tipo de formulários 'form.Form':
