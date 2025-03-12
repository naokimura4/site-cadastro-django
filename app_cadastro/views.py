from django.shortcuts import render
from .models import Usuario
def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    # Dados salvos para o DB
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade') 
    novo_usuario.save()
    # Exibir informações em uma nova pagina
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    
    return render(request, 'usuarios/usuarios.html',usuarios)