####### cria aplicações #######
#criar venv
python -m venv venv

#ativar venv
cd Scripts
cd bin
.\activate
resolver problema de permissão windows ``` Set-ExecutionPolicy RemoteSigned ```
 source ./activate <- linux
 #desativar
 deactivate

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
#restartar nginx
sudo /etc/init.d/nginx restart
#conectar nginx com uwsgi
uwsgi --socket :8001 --wsgi-file test.py
uwsgi --socket mysite.sock --module mysite.wsgi --chmod-socket=664
#criar arquivo mysite_uwsgi.ini
uwsgi --ini mysite_uwsgi.ini
#configurar inicialização por systemctl
https://uwsgi-docs.readthedocs.io/en/latest/Systemd.html
# deixar o arquivo com permissão 664 uwsgi_gestao_rh.service

#Ajax

#integrar django com jquery

#criação de api
#instalar django rest
pip install djangorestframework
#rodar migrate
#criar arquivo serializers.py na app core
#criar view e url
#registrar app no settings

#celery
https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html
#installar redis
sudo apt-get install redis
#verificar status do redis
sudo /etc/init.d/redis-server status
#testar celery
sudo celery -A gestao_rh worker -l info
windows:
sudo celery -A gestao_rh worker --pool=solo -l info
https://github.com/rgl/redis/downloads

python manage.py shell
from gestao_rh.celery import debug_task
debug_task.delay()

#enviar email
no servidor incluir usuário e senha no arquivo settings.
ativar apps menos seguros google: https://myaccount.google.com/lesssecureapps
liberar um novo disposito: https://accounts.google.com/DisplayUnlockCaptcha

#tarefa agenda com celery beat
celery -A gestao_rh beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
#no linux rodas celery e celery beat juntos
celery -A gestao_rh worker -B

#incluir celery no systemctl

###### Instalar certificado auto assinado. #####
# sudo apt-get install openssl
# which openssl
# mkdir /usr/local/nginx/ssl
# openssl req -x509 -nodes -newkey rsa:2048 -keyout cert.key -out cert.crt -days 365
##https://adrianorosa.com/blog/nginx/configurar-nginx-https-server-com-self-signed-ssl-certificado.html

# configurando multiplos bancos de dados

- migrate com database antigo
python manage.py migrate --database=antigo
- criar routers de databases
DATABASE_ROUTERS = ['gestao_rh.DBRoutes.DBRoutes']
- django zerar banco
python manage.py flush
 - tabela já existi, passar o fake
 python manage.py migrate --database=antigo --fake

# atualizando banco de dados manualmente
python manage.py shell
from apps.empresas.models import *
Empresa.objects.using('antigo').create(nome='Minha empresa antiga')
Empresa.objects.all()
Empresa.objects.using('antigo').all()




