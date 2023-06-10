from django.urls import path
from .views import index

# Criação da rota:
urlpatterns = [
    path('', index, name='index'),
]

