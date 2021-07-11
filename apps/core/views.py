from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.funcionarios.models import Funcionario
from .tasks import send_relatorio

@login_required
def home(request):
    data = {}
    data['usuario'] = request.user
    return render(request, 'core/index.html', data)

def celery(request):
    send_relatorio.delay()
    return HttpResponse('Tarefa incluida na fila para execução.')

from django.contrib.auth.models import User
from rest_framework import viewsets
from apps.core.serializers import UserSerializer

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
