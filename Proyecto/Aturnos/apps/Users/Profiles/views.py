from django.shortcuts import render,redirect
from .models import Users
from .forms import UsuarioForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
@login_required
def data(request):
    person =Users.objects.all()
    contexto={
        'person':person
    }
    return render (request, 'index.html',contexto)

def exit(request):
    logout(request)
    return redirect('/')

@login_required
def createUser(request):
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

@login_required
def editUser(request,id):
    usuario = Users.objects.get(id = id)
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

@login_required
def  deleteUser(reques,id):
    usuario = Users.objects.get(id = id)
    usuario.delete()
    return redirect('index')