# Create your tasks here

from celery import shared_task
#from apps.core.models import Widget
from django.core.mail import send_mail
from apps.funcionarios.models import Funcionario

@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)

@shared_task
def send_relatorio():
    total = Funcionario.objects.all().count()
    send_mail(
        'Relatório celery',
        'Relatório geral de funcionario %f' % total,
        'caz.carlos@gmail.com',
        ['carlos.desousa91@outlook.com'],
        fail_silently=False,
    )
    return True

#@shared_task
#def count_widgets():
#   return Widget.objects.count()


#@shared_task
#def rename_widget(widget_id, name):
#    w = Widget.objects.get(id=widget_id)
#    w.name = name
#    w.save()