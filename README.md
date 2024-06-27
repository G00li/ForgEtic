# Bem vindo ao ForgEtic! 


## Nosso objetivo 🎯: 

"Ter seus arquivos importantes sempre à mão pode fazer toda a diferença na sua produtividade e tranquilidade. Com ForgEtic, você tem a certeza de que seus documentos, fotos e vídeos estão sempre disponíveis, onde quer que você esteja.Esqueça as preocupações com a segurança e a acessibilidade dos seus arquivos – o ForgEtic está aqui para simplificar sua vida digital"

Com esta frase que o ForgEtic surge. 
O objetivo do projeto foi reinventar uma drive, possibilitando os users não só salvarem seus documentos, mas também possibilita o Download e gestão de todos os ficheiros existentes lá. Podendo criar pastas dentro de pastas e salvar files onde desejar, seja na root ou dentro de outras folders ao seu desejo.  



## Organização do projeto〘💻〙: 

### Tree do projeto: 
```
├── Dockerfile
├── ForgEtic
│   ├── __init__.py
│   ├── asgi.py
│   ├── middlewares.py
│   ├── settings.py
│   ├── static
│   │   └── Css
│   │       ├── file.css
│   │       ├── folder.css
│   │       ├── initialPage.css
│   │       └── style.css
│   ├── templates
│   │   ├── base.html
│   │   └── index.html
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── app_upload
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── templates
│   │   ├── folderContent.html
│   │   └── folderView.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── app_usuarios
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── templates
│   │   ├── cadastro.html
│   │   ├── formResetPass.html
│   │   └── login.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── Makefile
├── README
├── docker-compose.yaml
├── manage.py
├── poetry.lock
├── pyproject.toml
```


O projeto é dividido em 1 pasta projeto e 2 apps:
	1. ForgEtic
	2. app_usuário
	3. app_upload

#### ForgEtic: 
   Esta pasta é a root do projeto, onde está o ficheiro settings.py com toda a definição de utilização do Django. Além disso, toda a estrutura base do html se encontra no ficheiro Template, dividido em base.html e index.html. 
   
   **HTML:**
	   O base.html é onde se encontra todo o esqueleto do site, definindo suas alturas e larguras. 
	   O index.html é uma extensão do bloco 'semLogin' do base.html. Nesse html específico, é onde se encontra a pagina inicial de login / register do utilizador. 

**Static/Css:**
	é onde contem toda a estilização do projeto. 
	subdividido em 4 pastas, cada uma com a sua estilização específica: 
- File.css ➯ Css responsável pela estilização dos Files
- Folder.css ➯ Css responsável pela estilização do Folders
- InitialPage.css ➯ Css responsável pela página quando nenhum usuário esteja logado
- Style.css ➯ Css raiz de todo o esqueleto do site


#### App_usuário:
Assim como o folder ForgEtic, a app_usuário, como o próprio nome diz, é uma app responsável por todo o sistema de login e register do usuário.


 **HTML**
Nos templates, constam todos os Htmls necessários para o login, Sign Up e Reset Password do utilizador. 
Todos os htmls estendem do html raiz, que é o base.html, onde, através do Jinja2, é possível exibir o código de forma automática dependendo do botão que o utilizador escolher.


**Views/ Urls**
Todas a parte lógica do programa se encontram em funções no file `Views.py`, onde eles se comunicam com as urls existente no file `Urls.py` e inserem a lógica no Html através do name da path no url (onde basicamente são "variáveis"). 



#### App_upload: 
Nessa aplicação, se encontra toda a lógica existente após o utilizador ter passado pela parte da autenticação.
Basicamente, toda a lógica de criação, edição e excluir os files e folders são funções existentes dentro da `Views.py`. Que assim como no App_usuários, se comunicam com as `Urls.py` e implementam a lógica no HTML. 


Com essas 3 Folders em sincronia, o projeto consegue fazer upload, download e delete dos folders e files. 

## Processo de instalação : 

Nosso aplicativo se encontra disponível em um [repositório Github](https://github.com/G00li/ForgEtic), completamente gratuito e de fácil acesso. 

**Nota:** Para sua melhor experiencia, recomendamos a utilização da versão mais recente. Isto é, a versão mais atualizada das [Tags disponíveis](https://github.com/G00li/ForgEtic/tags).

**Nota 2:** Todo o processo de instalação usará o Visual Studio Code (VSCode) como exemplo. Caso não tenha instalado em sua maquina, [clique aqui](https://code.visualstudio.com/download) será redirecionado para o site oficial do VSCode. 

Para instalar o ForgEtic, basta seguir os 6 passos abaixo: 
1. Clonar o [repositório do projeto](https://github.com/G00li/ForgEtic) 
2. Ter um editor de código-fonte recomendado ([VSCode](https://code.visualstudio.com/))
3. Abrir o repositório clonado através do VSCode 
4. Será exibido uma mensagem no canto inferior direito, perguntando se deseja abrir em um container de desenvolvimento. Recomendamos clique em *Reabrir no Contêiner* 
5. Execute no terminal do VSCode o comando: `make up`
		onde, através desse comando, será instalado todas as dependências necessárias para o projeto funcionar.
6. Acessar o seu [Localhost](http://localhost:8000)

Após seguir esses passos corretamente, voce poderá usufruir de todas as funcionalidades do ForgEtic. 


### Criando um admin:

#### De forma automática:
Para criar um admin de forma automática dentro do projeto, é necessário executar o comando (no terminal do VSCode) `make create-admin-automatico`, onde será atribuído de forma automática os seguintes dados para o seu admin. 
	username: admin
	email: admin@example.com
	
A password será pedida ao seu critério. 


#### De forma manual: 
Para criar um admin de forma manual dentro do projeto, é necessário executar o comando(no terminal do VSCode) `make create-admin-manual` onde será a requisitado o username, email e password do novo admin. 


### Acessando a parte Admin 
Para acessar a area Admin do projeto, você deverá ter primeiramente uma conta de admin válida (caso ainda não tenha, consulte o tópico *Criando um admin*). 
Basicamente terá que aceder ao seu localhost utilizando o link http://localhost:8000 e adicionando o /admin após o 8000. 
Link para a sessão admin do projeto: http://localhost:8000/admin

Nesse link será requisitado o email e senha da conta admin. Onde após fazer a verificação, será exibida todas as funcionalidades de um admin. 



