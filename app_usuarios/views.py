from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def cadastro(request): 
    if request.method == "GET":
        return render (request, 'cadastro.html')
    else: 
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        contrasenha = request.POST.get('contraSenha')
        

        if senha != '' and contrasenha != '':
            if senha != contrasenha:
             # //TODO - Fazer uma melhor view para senhas diferentes
                messages.info(request, 'Senha diferente de Contra senha')
                return render(request, 'cadastro.html')
        
        user = User.objects.filter( username=username).first() 

        if user: # Confere se já existe algum username igual já cadastrado na base de dados 
            #TODO - Fazer uma melhor versão para quando o username já existe
            
            messages.info(request, 'O usuario ja existe')
            return render(request, 'cadastro.html')
            

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
            messages.info(request, 'Erro ao realizar login. Verifique seu username e senha.')
            return redirect ('login')


def user_logout (request):
    logout(request)
    return redirect('home')



@login_required(login_url="/login/") #REVIEW - Fazendo a verificação se o cliente está logado
def homePage (request): 
        return HttpResponse('plataforma')