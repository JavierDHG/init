from django.shortcuts import render,redirect
from .models import Usuarios
from .forms import UsuarioForm

# Create your views here.
def datos(request):
    persona =Usuarios.objects.all()
    contexto={
        'persona':persona
    }
    return render (request, 'index.html',contexto)

def crearUser(request):
    if request.method == 'GET':
        form = UsuarioForm()
        contexto = {
            'form':form
        }
    else:
        form = UsuarioForm(request.POST, request.FILES)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'crearUser.html',contexto)

def editarUser(request,id):
    usuario = Usuarios.objects.get(id = id)
    if request.method == 'GET':
        form = UsuarioForm(instance = usuario)
        contexto = {
            'form':form
        }
    else:
        form = UsuarioForm(request.POST, instance = usuario)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request,'crearUser.html',contexto)

def  eliminarUser(reques,id):
    usuario = Usuarios.objects.get(id = id)
    usuario.delete()
    return redirect('index')