from django.shortcuts import render
from .forms import UserForm

# Metodos HTTP(verbos):
"""
GET => Pega ou busca;
POST => Enviar dados 'embrulhados' no método post;
PUT => Geralmente usado para atualizações;
DELETE => Usado para remover um recurso.

"""

# Função para o 'index.html'

def index(request):
    return render(request,'user/index.html') 

# Função para o 'criar.html'

def create(request):
    if request.method == 'GET':
        form = UserForm()
        context = {
            'form':form,
        }
        return render(request, 'user/criar.html', context=context)
    else:
        form = UserForm(request.POST) # Verifica se o método declarado é válido e print o 'form'
        if form.is_valid():
            context = {
                'nome': form.cleaned_data['nome'],
                'telefone': form.cleaned_data['telefone'],
                'email': form.cleaned_data['email'],
            }
            
            return render(request, 'user/index.html', context=context) # Necessário para renderizar o 'form' para o template
def modify(request, user_id):
    context = {
        'id':user_id,
    }
    return render(request, 'user/index.html', context=context)
    

