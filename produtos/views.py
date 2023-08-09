from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa

def ver_produto(request):
    if request.method =="GET":
        nome = 'caio'
        return render(request, 'ver_produto.html', {'nome' : nome})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        
        pessoa = Pessoa(nome=nome, idade=idade)
        pessoa.save()
        return HttpResponse('Dados cadastrados com sucesso')


        # pessoas = Pessoa.objects.filter(nome=nome)
        # if pessoas.exists():
        #     print('usuario existente')
        # else:
        #     print('Usuario cadastrado')
        # return HttpResponse(pessoas)
    
        # pessoa = Pessoa(nome=nome, idade=idade)
        # pessoa.save()
        # metodo para cadastrar usuarios no banco de dados

        # pessoa = Pessoa(nome=nome, idade=idade)
        # pessoa.save()
        # return HttpResponse('Dados cadastrados com sucesso')
    


def inserir_produto(request):
    return HttpResponse('Estou no inserir')
