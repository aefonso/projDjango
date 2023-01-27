from django.urls import path
#from recipes.views import home, sobre, contato
from . import views

# HTTP Request
urlpatterns = [
    path('', views.home),
    path('recipe/', views.recipe),
    path('receitas2/', views.receitas2, name='receitas2'),
    path('receitas3/', views.receitas3, name='receitas3'),
    path('receitas/', views.receitas, name='receitas'),
]
