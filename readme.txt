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

