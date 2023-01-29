from django.urls import path
#from recipes.views import home, sobre, contato
from . import views
from django.conf.urls.static import static
from django.conf import settings

# HTTP Request
urlpatterns = [
    path('', views.home),
    path('recipe/', views.recipe),
    path('receitas2/', views.receitas2, name='receitas2'),
    path('receitas3/', views.receitas3, name='receitas3'),
    path('receitas/', views.receitas, name='receitas'),
    path('contatos1/', views.contatos1, name='contatos1'),
    path('contatos2/', views.contatos2, name='contatos2'),
    path('contatos3/', views.contatos3, name='contatos3'),
    path('static/recipes/css/styles.css', static(settings.STATIC_URL + 'recipes/css/styles.css')),
]
