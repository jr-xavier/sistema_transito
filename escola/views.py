from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'escola/index.html')

def processar_matricula(request):
    if request.method == 'POST':
        context = {
            'nome_aluno': request.POST.get('nome_aluno'),
            'data_nascimento': request.POST.get('data_nascimento'),
            'nome_escola': request.POST.get('nome_escola'), # Adicionado
            'nome_responsavel': request.POST.get('nome_responsavel'),
            'documento': request.POST.get('documento'),
            'telefone_1': request.POST.get('telefone_1'),
            'telefone_2': request.POST.get('telefone_2'),
        }
        return render(request, 'escola/contrato.html', context)