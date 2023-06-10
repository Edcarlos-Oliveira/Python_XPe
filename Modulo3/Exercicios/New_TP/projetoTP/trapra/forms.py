from django import forms
from .models import TestModel


# Criando as classes form:
class TestForm(forms.ModelForm):
    
    #Criando a classe Meta:
    class Meta:
        model = TestModel
        # Especificando os fields que serão usados:
        fields = ['a', 'b', 'c']
        


        
    
            
                                         
