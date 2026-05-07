from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('processar_matricula/', views.processar_matricula, name='processar_matricula'),
]