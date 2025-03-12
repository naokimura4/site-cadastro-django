from django.urls import path
from app_cadastro import views

urlpatterns = [
    path('', views.home,name='home'), # rota, view, nome_ref
    path('usuarios/', views.usuarios, name='listagem_usuarios')
]
