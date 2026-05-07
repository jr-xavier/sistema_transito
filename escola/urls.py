from django.urls import path
from . import views

urlpatterns = [
    # Ajustado para 'home' para bater com sua views.py
    path('', views.home, name='index'), 
    
    # Rota para o processamento dos dados
    path('processar_matricula/', views.processar_matricula, name='processar_matricula'),
]