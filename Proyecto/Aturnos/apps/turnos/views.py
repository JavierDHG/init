from django.shortcuts import render,redirect
from .models import Turns
from .forms import TurnsForm

# Create your views here.

def turn(request):
    turn = Turns.objects.all()
    contexto ={
        "turn": turn
    }
    return render(request, 'turno.html', contexto)

def createTurn(request):
    if request.method == 'GET':
        form = TurnsForm()
        contexto = {
            'form':form
        }
    else:
        form = TurnsForm(request.POST)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('turno')
    return render(request,'crearTurno.html',contexto)

def editTurn(request,id):
    turn = Turns.objects.get(id = id)
    if request.method == 'GET':
        form = TurnsForm(instance = turn)
        contexto = {
            'form':form
        }
    else:
        form = TurnsForm(request.POST, instance = turn)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('turno')

    return render(request,'crearUser.html',contexto)

def  deleteTurn(reques,id):
    turn = Turns.objects.get(id = id)
    turn.delete()
    return redirect('turno')