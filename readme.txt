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

#ciar super usuário
python manage.py createsuperuser

#criar app
python manage.py startapp

#registrar app
INSTALLED_APPS = [
'apps.empresas',

#definir model

#importar model


