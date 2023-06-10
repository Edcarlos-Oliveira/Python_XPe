from django.shortcuts import render
from .models import TestModel
from .forms import TestForm
from math import sqrt


# Criando as funções:
def index(request):
    if request.method == 'GET':
        form = TestForm()
        context = {
            'form':form,
        }
        return render(request, 'user/index.html', context=context)
    else:
        form = TestForm(request.POST)
        if form.is_valid():

            while True:
                try:
                    a = form.cleaned_data['a']
                    b = form.cleaned_data['b']
                    c = form.cleaned_data['c']
                    
                    delta = b * b - 4 * a * c
                    r1 = (- b + sqrt(delta)) / (2 * a)
                    r2 = (- b - sqrt(delta)) / (2 * a)
                except(ValueError, TypeError, AttributeError, UnboundLocalError):
                    context = {
                        'form': {'ERROR: Os valores digitados não têm raízes reais!!!'}
                    }
                    return render(request, 'user/index.html', context=context)
                else:
                    context = {
                        'form': form,
                        'a': delta,
                        'b': r1,
                        'c': r2,                                                                  
                    }
                    return render(request, 'user/index.html', context=context)  

