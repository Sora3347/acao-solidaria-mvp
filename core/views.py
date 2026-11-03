
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Item, Familia

def dashboard(request):
    return render(request, 'core/index.html')

def cadastrar_doacao(request):
    if request.method == 'POST':
        messages.success(request, 'Doação cadastrada com sucesso!')
        return redirect('dashboard')
    return render(request, 'core/cadastrar.html')

def entregas(request):
    if request.method == 'POST':
        messages.success(request, 'Entrega confirmada com sucesso!')
        return redirect('entregas')
    return render(request, 'core/entrega.html')
