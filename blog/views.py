
from django.shortcuts import render, redirect
from .models import Produto
from .forms import FormularioProduto
# Create your views here.


def home(request):
    produtos = Produto.objects.all()
    data = {}
    data['produtos'] = produtos

    return render(request, 'blog/home.html', data)

def create(request):
    form = FormularioProduto(request.POST or None)
    data = {}
    data['form'] = form

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'blog/create.html', data)

def read(request, pk):
    produtos = Produto.objects.get(pk=pk)
    data = {}
    data['produtos'] = produtos

    return render(request, 'blog/produto.html', data)

def update(request, pk):
    produtos = Produto.objects.get(pk=pk)
    form = FormularioProduto(request.POST or None, instance=produtos)
    data = {}
    data['produtos'] = produtos
    data['form'] = form

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'blog/update.html', data)

def delete(request, pk):
    Produto.objects.get(pk=pk).delete()

    return redirect(home)