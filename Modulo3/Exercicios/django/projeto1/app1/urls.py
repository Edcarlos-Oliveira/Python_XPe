from django.urls import path
from .views import index, create, modify

# Criação de rotas:
urlpatterns = [
    path('',index,name='index'),
    path('criar/', create, name='criar'),
    path('modificar/<int:user_id>', modify,name='modify'), # utilizando 'query params(<int:user_id>)'
]
