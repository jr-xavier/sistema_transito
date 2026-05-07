from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # ou views.index, dependendo do nome da sua função
    path('processar/', views.processar_matricula, name='processar_matricula'),
]