####### cria aplicações #######
#criar venv
 python -m venv venv

#ativar venv
cd Scripts
cd bin
.\activate

#instalar django na raiz 
pip install django

#criar projeto django
django-admin startproject gestao_rh .

#executar projeto
python manage.py runserver

#criar banco
python manage.py migrate

#ciar super usu�rio
python manage.py createsuperuser

#criar app
python manage.py startapp

#registrar app
INSTALLED_APPS = [
'apps.empresas',

#definir model

#importar model

#git remover arquivos incluidos por engano
git rm --cache __pycache__ -r

##########views e templates ##########

#definir caminho dos templates
'DIRS': ['templates'],

#alterar idioma e time zone
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'

#criar template base.html

#criar urls

#criar views

#criar app core

########## integrar com bootstrap #########

#baixar bootstrap no diretório static

#chamar o template no base.html

# incluir caminho dos arquivo estaticos.
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

########## chamar url account #########

#criar template registration

#criar variavel padrão LOGIN_REDIRECT_URL

#criar login_required no metodo home

#criar variavel padrão LOGOUT_REDIRECT_URL

########## criar crud empresas #########

########## criar crud funcionarios ##########

########## criar crud departamentos ##########
    #linkar urls
    #criar views
    #alterar models
    #criar templates

######### instalar bootstrap form ##########

pip install django-bootstrap-form

INSTALLED_APPS = (
    ...
    'bootstrapform',
    ...
)
# loadbootstrap

######### crud documentos #########

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

########## crud banco de horas ##########

########## Deploy ##########

#criar vm na AWS

#configurar maquina
ssh -i "gestao_rh.pem" ubuntu@ec2-18-228-165-176.sa-east-1.compute.amazonaws.com
sudo apt-get update && sudo apt-get upgrade
#instalar venv
apt-get install python3-venv
#criar venv
python -m venv venv
#ativar venv
source venv/bin/activate
#gerar requirements
pip freeze > requirements.txt
#clonar projeto para o servidor
#instalar requirements
pip install -r requirements.txt
# instalar uwsgi
pip install uwsgi
#criar arquivo de teste e rodar
uwsgi --http :9090 --wsgi-file foobar.py
#rodar o projeto com o uwsgi
uwsgi --http :8080 --wsgi-file gestao_rh/wsgi.py
#instalar nginx
sudo apt-get install nginx
#criar arquivo uwsgi_params dentro da pasta do projeto
#incluir parametros https://github.com/nginx/nginx/blob/master/conf/uwsgi_params
#criar arquivo /etc/nginx/sites-available/mysite_nginx.conf
https://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html
#criar link simbolico em /etc/nginx/sites-enabled/
sudo ln -s /etc/nginx/sites-available/gestao_rh.conf
#criar arquivo static_root
STATIC_ROOT = os.path.join(BASE_DIR, "static/")
python manage.py collectstatic

