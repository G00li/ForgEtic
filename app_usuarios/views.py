from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required



def cadastro(request): 
    if request.method == "GET":
        return render (request, 'cadastro.html')
    else: 
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        # //TODO - Criar confirmação de senha -> confirmacao_senha = request.POST.get('confirmacao_senha')
        
        user = User.objects.filter( username=username).first() 

        if user: # Confere se já existe algum username igual já cadastrado na base de dados 
            return HttpResponse("Username já cadastrado")

        user = User.objects.create_user(username=username, email=email, password=senha) #//NOTE - Criando o user e associando seus atributos
        user.save()

        # return HttpResponse("Ususario cadastrado com sucesso!")
        return redirect('login')


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username = username, password = senha) #recebendo os dados inseridos e conferindo com a base de dados 

        if user:
            login_django(request, user)
            return redirect('home')
        
        else:
            return HttpResponse("Erro ao realizar login. Verifique seu username e senha.")
        

# @login_required(login_url="/login/")
# def logout(request):
#     return redirect ('home')


def user_logout (request):
    logout(request)
    return redirect('home')



@login_required(login_url="/login/") #REVIEW - Fazendo a verificação se o cliente está logado
def homePage (request): 
        return HttpResponse('plataforma')