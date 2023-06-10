from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User

# Rota que renderiza o 'index.html'.
def index(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request,'index.html', context)

# Rota que cria novo usuário e retorna para o index:
def create(request):
    if request.method == 'GET':
        form = UserForm()
        context = {
            'form': form,
        }
        return render(request, 'criar.html', context=context)
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index) 

# Rota que atualiza o usuário e retorna para o index:
def refresh(request, user_id):
    user = User.objects.get(pk=user_id) # Verifica o objeto 'pk(primary key)'

    if request.method == 'POST':
        form = UserForm(data=request.POST, instance=user) # Pega um modificado para modificar

        if form.is_valid():
            form.save()
            return redirect(index) 
    else:
        form = UserForm(instance=user) # Quando o usuário clica para modificar

        context = {
            'form': form,
        }
        return render(request,'criar.html', context=context)

# Rota para deletar o usuário:
def delete(request, user_id):
    user = User.objects.get(pk=user_id)
    user.delete()
    return redirect(index)


    
