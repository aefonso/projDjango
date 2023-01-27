from django.shortcuts import render
from django.http import HttpResponse
from utils.recipes.factory import make_recipe
# Create your views here.

# HTTP Request
def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'recipes': [make_recipe() for _ in range(9)], 'name': 'SoolQueijo',
    })

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page' : True,
    })

def receitas(request):
    return render(request, 'recipes/pages/receitas.html', context={'name': 'Hamburger'})

def receitas2(request):
    return render(request, 'recipes/pages/receitas2.html', context={'name': 'Hamburger'})

def receitas3(request):
    return render(request, 'recipes/pages/receitas3.html', context={'name': 'Hamburger'})

def contatos1(request):
    return render(request, 'recipes/pages/contatos1.html', context={'name': 'Chefe'})

def contatos2(request):
    return render(request, 'recipes/pages/contatos2.html', context={'name': 'Chefe'})

def contatos3(request):
    return render(request, 'recipes/pages/contatos3.html', context={'name': 'Chefe'})
  
def contato(request):
    # HTTP Response
    return HttpResponse('')
